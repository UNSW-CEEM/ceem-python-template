import logging
from datetime import datetime
from typing import List, Optional

from attrs import define, field
from dateutil import rrule

from .dl_helpers.functions import (
    _construct_sqlloader_forecastdata_url,
    get_historical_forecast_tables,
    get_sqlloader_filesize,
    get_unzipped_csv,
)
from .loader import Loader

logger = logging.getLogger(__name__)


def _enumerate_tables(tables: List[str], table_str: str, range_to: int):
    """Given a table name, populates a list with enumerated table names

    For example, given 'CONSTRAINTSOLUTION' and `range_to`=3, will populate
    `tables` with ['CONSTRAINTSOLUTION1',...,'CONSTRAINTSOLUTION3'].

    Args:
        tables: Table list
        table_str: Table string to enumerate
        range_to: Integer to enumerate to
    Returns:
        `tables` with enumerated `table_str`
    """
    tables.remove(table_str)
    for i in range(1, range_to + 1):
        tables.append(f"{table_str}{i}")
    return tables


def _validate_tables_on_forecast_start(instance, attribute, value):
    """Validates tables for the provided forecast type.

    Checks user-supplied tables against tables available in MMS Historical
    Data SQL Loader for the month and year of forecast_start.
    """
    start_dt = instance.forecast_start
    tables = get_historical_forecast_tables(
        start_dt.year, start_dt.month, instance.forecast_type
    )
    if not set(value).issubset(set(tables)):
        raise ValueError(
            "Table not available from MMS Historical Data SQL Loader"
            + f" (for {start_dt.month}/{start_dt.year}).\n"
            + f"Tables include: {tables}"
        )


@define(kw_only=True)
class ForecastTypeDownloader:
    forecast_start: datetime
    forecast_end: datetime
    forecast_type: str
    tables: List[str] = field(validator=_validate_tables_on_forecast_start)
    raw_cache: Optional[str] = field(default=None)

    @classmethod
    def from_Loader(cls, loader: Loader):
        """Constructor method for ForecastTypeDownloader from Loader."""
        tables = loader.tables
        if "CONSTRAINTSOLUTION" in tables:
            tables = _enumerate_tables(tables, "CONSTRAINTSOLUTION", 4)
        return cls(
            forecast_start=loader.forecast_start,
            forecast_end=loader.forecast_end,
            forecast_type=loader.forecast_type,
            tables=tables,
            raw_cache=loader.raw_cache,
        )

    def download_zip(self):
        """Downloads zip files given query loaded into ForecastTypeDownloader

        .. todo:: Extend to converting to parquet
        """
        intervening_dates = rrule.rrule(
            rrule.MONTHLY, dtstart=self.forecast_start, until=self.forecast_end
        )
        for table in self.tables:
            for date in intervening_dates:
                (year, month) = (date.year, date.month)
                url = _construct_sqlloader_forecastdata_url(
                    year, month, self.forecast_type, table
                )
                size = get_sqlloader_filesize(year, month, self.forecast_type, table)
                logger.info(
                    f"Downloading {table} for {month}/{year}: {size} MB (zipped)"
                )
                get_unzipped_csv(url, self.raw_cache)

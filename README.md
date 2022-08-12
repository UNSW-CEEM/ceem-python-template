# UNSW CEEM Python Package Template

Replace the heading above with `your_package`.

---

Badges can go here

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## How do I use this template?

1. Hit "*Use this template*" in the top right of this page
2. Work through as much of the [basic](https://github.com/UNSW-CEEM/ceem-python-template#basic), [intermediate](https://github.com/UNSW-CEEM/ceem-python-template#intermediate) and [advanced](https://github.com/UNSW-CEEM/ceem-python-template#advanced) steps as you like.
3. Edit this README and make sure you update `your_package`, `your_name` and `licence_type`.

### References

Nothing helps as much as examples.
- [This](https://www.marwandebbiche.com/posts/python-package-tooling/) is a great guide that provides a brief overview of all the tools we use in this template.
- All of the tooling has been implemented in [`nemseer`](https://github.com/UNSW-CEEM/NEMSEER)


## Usage

### Basic

#### Updating repo info

1. [Choose a license](https://choosealicense.com/), and add the `LICENSE` file to the repo
2. Update your [code of conduct](CONDUCT.md)
3. Update the [*Get Started!* section](CONTRIBUTING.md#get-started) of the [contributing guidelines](CONTRIBUTING.md)
    - Note that this currently has steps you would use to install poetry v1.2.0b2 and various dependency groups that are being used by [`nemseer`](https://github.com/UNSW-CEEM/NEMSEER)
4. (Optional) [Make your software citeable](https://citation-file-format.github.io/)

#### Poetry

1. Install [`poetry`](https://python-poetry.org/docs/master/)
    - Note that this repo is using poetry v1.2.0b2, so install this version (see the [contributing guidelines](CONTRIBUTING.md#get-started)) 
    - As of August 2022, 1.2.0 is still pre-release, so make sure you are on the `master` version of the poetry documentation
    - Edit the project info in [`pyproject.toml`](pyproject.toml), or delete it and use `poetry init` to start from scratch (if you are proceeding to the next few sections, it is best not to delete the existig `pyproject.toml`)
    - You can add dependencies in the [`pyproject.toml`](pyproject.toml) or use the command line:
      - You can add a core dependency via `poetry add pandas` 
      - You can add dependencies to a group (adding to a group is optional) using `poetry add pytest --group test`
      - You can install the dependencies from `poetry.lock`, including optional groups, using `poetry install --with=test`
      - You can update dependencies and create a `poetry.lock` file using `poetry update`
      - **Commit `pyproject.toml` and `poetry.lock` to version control**

### Intermediate
      

### Advanced

## Contributing

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md), which also includes steps to install `your_package` for development.

Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`your_package` was created by `your_name`. It is licensed under the terms of the `licence_type`.

## Credits

This template was created using [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/), the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter) and using Marwan Debbiche's excellent [walkthrough](https://www.marwandebbiche.com/posts/python-package-tooling/)

# qBay - Python-CL-2021 front-end testing

[![Pytest-All](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/pytest.yml/badge.svg)](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/style_check.yml/badge.svg)](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/style_check.yml)

This image is the scrum board of A4 (frontend testing).
<p align="center">
  <img width="1000"  src="https://github.com/BerBer-alt/CISC327_Group8/blob/c215f3816df3f5dc067e005f058a9e369cc10013/Assign4_Scrum_Board.png">
</p>

This folder contains the files for A4 (frontend testing). Folder structure:

```
├── LICENSE
├── README.md
├── .github
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)
│       └── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)
├── qbay                 ======> Application source code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── __main__.py      ======> Program entry point
│   └── models.py        ======> Data models
├── qbay_test            ======> Testing code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── conftest.py      ======> Code to run before/after all the testing
│   └── test_models.py   ======> Testing code for models.py
└── requirements.txt     ======> Dependencies
```

To run the application module (make sure you have a python environment of 3.5+)

```
$ pip install -r requirements.txt
$ python -m qbay
```

Currently it shows nothing since it is empty in the `__main__.py` file.
Database and the tables will be automatically created into a `db.sqlite` file if non-existed.

To run testing:

```
# style check (only show errors)
flake8 --select=E .  

# run all testing code 
pytest -s qbay_test

```




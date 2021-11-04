# qBay - Python-CL-2021 front-end testing

[![Pytest-All](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/pytest.yml/badge.svg)](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/style_check.yml/badge.svg)](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/style_check.yml)

This image is the scrum board of A4 (frontend testing).
<p align="center">
  <img width="1000"  src="https://github.com/BerBer-alt/CISC327_Group8/blob/c215f3816df3f5dc067e005f058a9e369cc10013/Assign4_Scrum_Board.png">
</p>

### Daily Scrum - update
Each member in the team should at least answer to following questions:
```
1)what is the branch he/she worked on (has to be pushed to the repo).
2)what is the progress so far (at least some test cases written, more than 2)
3)any difficulties.
4)what is the plan for the days before the deadline.
```

Yifan Zhu:
```
1. I worked on "sprint4-Irving" branch.
2. Input Partitioning, output Partitioning and Input Boundary Testing.
3. No difficulties so far.
4. Complete 3 black box testing methods for registering and updating profile.
```

Yucan Li:
```
1. I worked on "YBranch4.0" branch.
2. Input Partitioning, Input Boundary Testing and Output Partitioning
3. Finding difficult when apply Output Partitioning becasue the output of the update product function is hard to partition.
4. Finish all the testing method and make sure all the test can pass.
```

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




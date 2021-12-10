# qBay - Python-CLI-2021 front-end testing

[![Pytest-All](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/pytest.yml/badge.svg)](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/style_check.yml/badge.svg)](https://github.com/BerBer-alt/CISC327_Group8/actions/workflows/style_check.yml)

This image is the scrum board of A5 (Testing & Deployment).
<p align="center">
  <img width="1000"  src="https://github.com/BerBer-alt/CISC327_Group8/blob/main/Assign6_Scrum_Board.png">
</p>

### :beer:Daily Scrum - update
Each member in the team should at least answer to following questions:
```
1)what is the branch he/she worked on (has to be pushed to the repo).
2)what is the progress so far (at least some test cases written/some results/code available)
3)any difficulties.
4)what is the plan for the days before the deadline.
```

Yifan Zhu:
```
1. I worked on "sprint5-irving" branch.
2. Completed setting up docker and docker compose. 
3. No difficulties so far.
4. Set up a meeting and complete code injection testing.
```

Yucan Li:
```
1. I worked on "YBranch6.0" branch.
2. Finish the front end for the brand new feature and make outstanding progress in security testing
3. Finding difficult when coding and implement iteration in db database 
4. Finish all the security testing cases and make sure all the test can pass and no more bugs.
```

Wenran Hou:
```
1. I worked on "hwr_sprint5" branch.
2. I use 'Generic_SQLI.txt' to test create product function.
3. Compare real outputs with expecting outputs.
4. Make sure all tests are passed.
```

Yiming Zheng:
```
1.I am working on Reg_test_inj  branch.
2.I am still writing pytest cases for regoster.
3.Not any difficulties so far.
4.It will be finished by tomorrow.

```


This folder contains the files for A4 (frontend testing). Folder structure:

```
├── LICENSE
├── README.md
├── .github
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)
│       └── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)
├── qbay                        ======> Application source code
│   ├── __init__.py             ======> Required for a python module (can be empty)
│   ├── __main__.py             ======> Program entry point
│   └── models.py               ======> Data models
├── qbay_test                   ======> Testing code
│   ├── __init__.py             ======> Required for a python module (can be empty)
│   ├── conftest.py             ======> Code to run before/after all the testing
│   ├── frontend                ======> Front End Testing Method
│   │   ├── __init__.py         ======> Required for a python module (can be empty)
│   │   └── test_update_product ======> Testing product update
│   │       ├── __init__.py                 ======> Required for a python module (can be empty)
│   │       ├── partition1.in               ======> #1 InputFile for Input Partition Testing
│   │       ├── partition2.in               ======> #2 InputFile for Input Partition Testing
│   │       ├── partition3.in               ======> #3 InputFile for Input Partition Testing
│   │       ├── partition4.in               ======> #4 InputFile for Input Partition Testing
│   │       ├── partition5.in               ======> #5 InputFile for Input Partition Testing
│   │       ├── partition6.in               ======> #6 InputFile for Input Partition Testing
│   │       ├── partition7.in               ======> #7 InputFile for Input Partition Testing
│   │       ├── partition_failed.out        ======> Failed cases OutputFile for Input Partition Testing
│   │       ├── partition_succeed.out       ======> Succeed cases OutputFile for Input Partition Testing
│   │       ├── boundary1.in                ======> #1 InputFile for Input Boundary Testing
│   │       ├── boundary2.in                ======> #2 InputFile for Input Boundary Testing
│   │       ├── boundary3.in                ======> #3 InputFile for Input Boundary Testing
│   │       ├── boundary4.in                ======> #4 InputFile for Input Boundary Testing
│   │       ├── boundary5.in                ======> #5 InputFile for Input Boundary Testing
│   │       ├── boundary6.in                ======> #6 InputFile for Input Boundary Testing
│   │       ├── boundary_failed.out         ======> Failed cases OutputFile for Input Boundary Testing
│   │       ├── boundary_succeed.out        ======> Succeed cases OutputFile for Input Boundary Testing
│   │       ├── outputPartition1.in         ======> #1 InputFile for Output Partition Testing
│   │       ├── outputPartition2.in         ======> #2 InputFile for Output Partition Testing
│   │       ├── outputPartition_failed.out  ======> Failed cases OutputFile for Output Partition Testing
│   │       ├── outputPartition_succeed.out ======> Succeed cases OutputFile for Output Partition Testing
│   │       ├── test_update_product.in      ======> InputFile for Testing product update
│   │       ├── test_update_product.in      ======> OutputFile for Testing product update
│   │       ├── test_update_product_boundary.py         ======> Python file for Input Boundary Testing
│   │       ├── test_update_product_outputPartition.py  ======> Python file for Output Partition Testing
│   │       └── test_update_product_partition.py        ======> Python file for Input Partition Testing
│   └── test_models.py          ======> Testing code for models.py
└── requirements.txt            ======> Dependencies
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




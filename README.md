# api-testing-project
## Overview
This project implements:
1. A RESTful API service for testing purpose
2. Automated tests implemented against the API service

The API endpoints return mocked data, produced by a data factory. This way
we don't have to implement the persistence layer nor use any third party mocking
framework such Wireframe or Mockoon.

## Tech stack
1. FastAPI - Python API framework
2. Pytest-BDD - Gherkin framework on top of pytest, which allows BDD style automation
3. Pylint - Python code linting
4. Faker - for generating test data such names, dates, numbers, streets, etc
5. Pytest-html-reporter - HTML test report plugin
6. Python 3.11

## Requirements
1. python 3.11+
2. pip3

## Setup
1. cd api-test-project
2. Create virtual environment: `python3 -m venv testenv`
3. Activate virtual environment: `source testenv/bin/activate`
4. Install packages: `pip3 install -r requirements.txt`

## Run API service
Run the following command to start the service background:
```fastapi dev main.py &```
Note: If you prefer to run in the foreground, you need a second terminal, where
you execute the setup procedures.

## Running tests
To run tests, execute the command:
```pytest```
The test will finish in less than a minute and the results displayed in the terminal.
An HTML test report is produced in the file:
```report/report.html```
Open the file in a browser for better and detailed view of the results

## Project structure
```
/api-testing-project
  /.github - Github workflow for CI
  /mocked-api
    /src
      /repository - data factory
      /routers - controllers
      /schemas - object schemas
      /services - service layer; serve controllers with mock data from the factory
      /utility - general purpose libraries
    main.py - main file
  /tests
    /integration
      /features - feature files; gherkin documents,which also service test documentation
      /fixtures - test data
      /step_defs - step definition files, containing implementation of test cases
      /utils - utility files
      conftest.py - test configuration file; we use this for setting environment, base url but we can also use for data seeking
      pytest.ini - another ini file; here we defined report options
  README.md
  requirements.txt
  api-testing-project.postman_collection.json - potsman collection for manual testing
```

## Test cases
The test cases are contained in two feature files under `tests/features` directory.
A feature file represents a test suite, which contains test scenarios.
A test scenario can have just one test case but can also have multiple data driven
test cases, in which case they are annotated as `Scenario Outline`. A scenario outline
will have example table, which contains rows of variables to be fed to the test.
Each row represents a test case, meaning the number to tests executed will depend
on the number of data rows.

## Known issues
We have had in issue with FastAPI, where it stops serving requires and responds to every
request `Invalid HTTP request`. This seems to have something to do with virtual environment
and only resolved when we exited virtual environment.






# Robot Framework Test Setup

## Overview

This repository contains Robot Framework test suites for testing an MS SQL Server database. The tests are written in Python and use the `pyodbc` library to connect to and interact with the database.

## Requirements

Before you can run the Robot Framework tests, you will need to have the following software installed on your machine:

- Python 3.7 or higher
- Robot Framework 4.0 or higher
- `pyodbc` library for Python
- MS SQL Server Management Studio (optional)

## Setup

To set up the test environment, follow these steps:

1. Clone the repository to your local machine.
2. Install Python 3.7 or higher on your machine, if it's not already installed.
3. Install Robot Framework by running the following command in your terminal:

    ```
    pip install robotframework
    ```

4. Install the `pyodbc` library by running the following command in your terminal:

    ```
    pip install pyodbc
    ```

5. (Optional) Install MS SQL Server Management Studio to interact with the database directly and verify the test results.

## Running the Tests

To run the tests, follow these steps:

1. Navigate to the root directory of the repository in your terminal.
2. Set `${SERVER}` variable to name of your MS SQL Server in `trn_database_test.robot` file. Windows Authentication is assumed.
3. Run the following command:

    ```
    robot trn_database_test.robot
    ```

4. Wait for the tests to complete. The test results will be displayed in the terminal.


# TRN Database Test Suite

This test suite uses pytest to test the functionality of the TRN database.

## Pre-requisites

1. **MS SQL Server is set up on local host.** You must have Microsoft SQL Server installed on your computer and ensure that it is running and accessible from your computer.
2. **Database TRN exists and current user can access it with Windows Authentication.** You should have a database named TRN set up in your SQL Server instance and have permission to access this database using Windows Authentication. If you are not sure how to set up a database or grant permissions, consult the SQL Server documentation or a database administrator.
3. **Python is installed.** You must have Python installed on your computer and ensure that it is accessible from your command prompt or terminal.
4. **Pytest is installed.** You must have the pytest testing framework installed in your Python environment. You can install pytest using the pip package manager by running the command
<br> 
```pip install pytest```
<br>in your command prompt or terminal.
5. **Allure is installed.** You must have the Allure test report generator installed on your computer. You can download and install Allure from the official Allure website and ensure that it is accessible from your command prompt or terminal:

## Setup
In the root test directory open *test_setting.py* file. Set SQL_SERVER_NAME property to the name of your MS SQL Server.

## Running the test
In order to run the tests use following command:<br>
```pytest tests_trn_db.py  --alluredir=./report```
<br>This command executes the tests and produce results in *./report* directory.

## Reporting test results
The test results are stored in *./report* directory. Using this data the Allure reports can be created.
Run the following command that start built-in web-server and displays Allure report:<br>
```allure serve .\report\```<br>
You may generate HTML-report that can be collected and deployed to another web-server:<br>
```allure generate ./report --clean -o ./report/html```
<br>

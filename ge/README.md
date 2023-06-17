# Running Great Expectations Notebook

This guide will walk you through the steps to run TRN database test suite with Great Expectations.
The test suite includes 3 Expectations:
- Expectation 1: Check if 'job_id' column has non-null values
- Expectation 2: Check if 'min_salary' is in defined range
- Expectation 3: Check if 'job_title' column has unique values

## Prerequisites

- Python 3.6 or higher
- Great Expectations installed (version 0.16.0 or higher)
- Jupyter Notebook installed
- MSSQL Server with TRN database is running

## Steps

1. Clone the repository:<br>
```git clone https://github.com/AlexeyBushnev/Pytest-DB-Test.git```

2. Navigate to the repository directory:<br>
```cd ./ge```

3. Start Jupyter Notebook:<br>
```jupyter notebook```

4. In the Jupyter Notebook interface, navigate to the notebook file: `ge_test.ipynb`

5. Update parameters of connection string to MSSQL Server

6. Open the notebook and execute each cell sequentially.

7. The last cell generates a test report. Review the results and verify if the expectations are met or not.

8. Make any necessary adjustments to the expectations or dataset as needed.

9. Save the notebook and exit Jupyter Notebook.

## Additional Resources
You can generate Data Docs report in readable HTML format:<br>
```great_expectations docs build```
Navigate to ```great_expectations/uncommitted/data_docs/local_site/``` directory and open ```index.html``` file with browser.

For more information on Great Expectations, please refer to the official documentation: [Great Expectations Documentation](https://docs.greatexpectations.io/)








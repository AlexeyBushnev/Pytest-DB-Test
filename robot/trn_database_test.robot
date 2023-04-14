*** Settings ***
Library    DatabaseLibrary
Documentation    'TRN' Database Testing in Robot Framework
Suite Teardown    Disconnect From Database

*** Variables ***
${DB_HOST}    localhost
${DB_NAME}    TRN
${SERVER}     XPGETBIW005C\\SQLEXPRESS
${DB_DRIVER}  com.microsoft.sqlserver.jdbc.SQLServerDriver
${DB_PORT}    1433

${DBHost_ConnectionString}=      Server='${SERVER}', Port='${DB_PORT}', Database='${DB_NAME}', Trusted_Connection='yes', Driver='{SQL Server}'

${output}

*** Test Cases ***
Connect to Database
   [Documentation]  Connect to Database. No errors from odbc driver are expected.
   Connect To Database Using Custom Params   pyodbc    ${DBHost_ConnectionString}
   

Table Column Completness Test
    [Documentation]  Current DB schema allows NULL and empty values. Check that regions have the notional names.
    ${output}=  Row Count Is 0    SELECT region_name FROM hr.regions WHERE region_name IS NULL OR LEN(region_name) < 2
    Log  ${output}
    	
Email Validation
    [Documentation]  Simple check does the records match email address format.
    ${output}=  Row Count Is 0    SELECT email FROM hr.employees WHERE email IS NOT NULL AND email NOT LIKE '%@%.%'
    Log  ${output} 

Uniqueness Of Values
    [Documentation]  Verify uniqueness of job titles.
    ${output}=  Row Count Is 0    SELECT job_title FROM hr.jobs GROUP BY job_title HAVING count(*) > 1
    Log  ${output}
import allure
import pytest
import pyodbc

from test_settings import SQL_SERVER_NAME


def get_db_connection_cursor():
    # pyodbc connection is auto closeable, no need to close manually
    return pyodbc.connect('Driver={SQL Server};'
                          f'Server={SQL_SERVER_NAME};'
                          'Database=TRN;'
                          'Trusted_Connection=yes;').cursor()


class TestDB:
    @pytest.mark.test_trn_db
    def test_simple_data_read(self):
        allure.dynamic.title("Simple test that check the Database is accessible and we can read the data.")
        rows = get_db_connection_cursor().execute("""SELECT * FROM hr.jobs""").fetchall()
        assert len(rows) > 0, \
            f"""Wrong number of fields!\nExpected: Number of rows is greater 0;\nActual: {len(rows)}"""

    @pytest.mark.test_trn_db
    def test_unique_job_titles(self):
        allure.dynamic.title("Verify uniqueness of job titles.")

        rows = get_db_connection_cursor() \
            .execute("""SELECT job_title 
                        FROM hr.jobs
                        GROUP BY job_title
                        HAVING count(*) > 1""") \
            .fetchall()
        assert len(rows) == 0, f"""No duplicated records are expected!\nThere are duplicates for {rows}!"""

    @pytest.mark.test_trn_db
    @pytest.mark.parametrize("budget", [100000, 120000, 130000])
    def test_minimal_budget(self, budget):
        allure.dynamic.title("Check that total salaries match the specified budget.")
        rows = get_db_connection_cursor() \
            .execute(f"""SELECT SUM(min_salary) 
                         FROM hr.jobs
                         HAVING SUM(min_salary) < {budget}""") \
            .fetchall()
        assert len(rows) == 0, \
            f"""The salary budget above {budget} is not allowed!\nActual: {rows}!"""

    @pytest.mark.test_trn_db
    @pytest.mark.parametrize("min_salary", [500, 1000, 3000])
    def test_min_salary(self, min_salary):
        allure.dynamic.title("Check that we have no salaries below the specified level.")
        rows = get_db_connection_cursor() \
            .execute(f"""SELECT min_salary 
                         FROM hr.jobs
                         GROUP BY min_salary
                         HAVING MIN(min_salary) < {min_salary}""") \
            .fetchall()
        assert len(rows) == 0, \
            f"""The salaries below {min_salary} are not allowed!\nThere are unexpected values: {rows}!"""

    @pytest.mark.test_trn_db
    def test_simple_email_validation(self):
        allure.dynamic.title("Simple validation of email addresses to standard compliance.")
        rows = get_db_connection_cursor() \
            .execute(f"""SELECT email
                         FROM hr.employees
                         WHERE email IS NOT NULL AND email NOT LIKE '%@%.%'""") \
            .fetchall()
        assert len(rows) == 0, \
            f"""The invalid emails have been found: {rows}!"""

    @pytest.mark.test_trn_db
    def test_dependents(self):
        allure.dynamic.title("Check on allowance of 'relationship' values.")
        rows = get_db_connection_cursor() \
            .execute(f"""SELECT relationship
                         FROM hr.dependents
                         WHERE relationship <> 'CHILD'""") \
            .fetchall()
        assert len(rows) == 0, \
            f"""Only 'CHILD' relationship is allowed, but there have been found: {rows}!"""

    @pytest.mark.test_trn_db
    def test_region_names(self):
        allure.dynamic.title("Current DB schema allows NULL and empty values. "
                             "Check that regions have the notional names.")
        rows = get_db_connection_cursor() \
            .execute(f"""SELECT region_name
                         FROM hr.regions
                         WHERE region_name IS NULL OR LEN(region_name) < 2""") \
            .fetchall()
        assert len(rows) == 0, \
            f"""The name of region should notional, but there have been found not allowed names: {rows}!"""

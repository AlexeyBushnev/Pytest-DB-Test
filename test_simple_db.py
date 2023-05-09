import allure
import pytest
import pymssql

from test_settings import SQL_SERVER_NAME
from test_settings import USERNAME
from test_settings import PASSWORD


def get_db_connection_cursor2():
    # pyodbc connection is auto closeable, no need to close manually
    return pymssql.connect(host='host.docker.internal', server=SQL_SERVER_NAME, port='1433', user=USERNAME, password=PASSWORD)


class TestSimpleDB:
    @pytest.mark.test_trn_db
    def test_simple_data_read(self):
        allure.dynamic.title("Simple test that checks the Database is accessible and we can read the data.")

        conn = get_db_connection_cursor2()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM TRN.hr.jobs""")
        rows = cursor.fetchall()
        assert len(rows) > 0, \
            f"""Wrong number of fields!\nExpected: Number of rows is greater 0;\nActual: {len(rows)}"""
        

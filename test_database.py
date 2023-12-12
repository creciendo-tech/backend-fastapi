import pytest

import database

def test_valid_credentials():
    connection = database.create_db_connection("localhost", "user", "password", "db")
    assert connection is not None

def test_invalid_password():
    try:
        connection = database.create_db_connection("localhost", "user", "wrong_password", "test_db")
    except Error as e:
        assert connection is None
        assert "Error connecting to database" in e.args[0]

def test_query_execution():
    connection = database.create_db_connection("localhost", "user", "password", "db")
    database.execute_query(connection, "SELECT * FROM data")

def test_formatting_data():
    sample_data = [(1, "name", "desc", 10), (2, "name2", "desc2", 20)]

    # Assert formatted result matches expectation
    formatted = database.format_query_result(sample_data)  
    assert formatted == [
        {'id': 1, 'name': 'name', 'description': 'desc', 'price': 10},
        {'id': 2, 'name': 'name2', 'description': 'desc2', 'price': 20}
        ] 


 

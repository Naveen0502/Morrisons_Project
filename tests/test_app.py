import pytest
from app import app
@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
def test_home_text_stream(test_client):
    csv = "samp.txt"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "samp.txt")}
    response = test_client.post('/', data=data)
    assert response.status_code == 500
def test_home_Empty_stream(test_client):
    csv = "empty_file.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "empty_file.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
    assert b"Empty File" in response.data
def test_home_base_stream(test_client):
    csv = "base_data.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "base_data.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
def test_home_Data_issue_stream(test_client):
    csv = "data_test_structure_issue.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "data_test_structure_issue.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
    assert b"DATA STRUCTURE ISSUE" in response.data 
def test_home_one_row_stream(test_client):
    csv = "one_row.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "one_row.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200  
def test_home_Data_original_stream(test_client):
    csv = "original_data.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "original_data.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
def test_home_Data_upto_6_stream(test_client):
    csv = "original_data_upto_level_6.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "original_data_upto_level_6.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
def test_home_Data_upto_10_stream(test_client):
    csv = "original_data_upto_level_10.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "original_data_upto_level_10.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
def test_home_Data_duplicate_stream(test_client):
    csv = "original_one_level_data.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "original_one_level_data.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
def test_home_Data_columns_only(test_client):
    csv = "columns_only.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "columns_only.csv")}
    response = test_client.post('/', data=data)
    assert response.status_code == 200
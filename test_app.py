import pytest
import requests

def test_read_table():
    response = requests.get('http://localhost:8000/productos')
    assert response.status_code == 200
    assert response.json() == [
  {
    "id": 1,
    "name": "Item 1",
    "description": "Description 1",
    "price": 10
  },
  {
    "id": 2,
    "name": "Item 2",
    "description": "Description 2",
    "price": 20
  },
  {
    "id": 3,
    "name": "Item 3",
    "description": "Description 3",
    "price": 30
  },
  {
    "id": 4,
    "name": "Item 4",
    "description": "Description 4",
    "price": 40
  },
  {
    "id": 5,
    "name": "Item 5",
    "description": "Description 5",
    "price": 50
  },
  {
    "id": 6,
    "name": "Item 6",
    "description": "Description 6",
    "price": 60
  },
  {
    "id": 7,
    "name": "Item 7",
    "description": "Description 7",
    "price": 70
  },
  {
    "id": 8,
    "name": "Item 8",
    "description": "Description 8",
    "price": 80
  },
  {
    "id": 9,
    "name": "Item 9",
    "description": "Description 9",
    "price": 90
  },
  {
    "id": 10,
    "name": "Item 10",
    "description": "Description 10",
    "price": 100
  }
]
   

def test_read_root():
    response = requests.get('http://localhost:8000/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

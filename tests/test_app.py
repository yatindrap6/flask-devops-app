# tests/test_app.py
from app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps World! CI/CD Pipeline is Working" in response.data


# tests/test_app.py
from app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask DevOps App!" in response.data


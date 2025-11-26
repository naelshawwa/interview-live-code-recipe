import pytest
import json
from flask import Flask
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_get_recipes_with_credentials(client):
    response = client.get('/api/recipes?q=chicken')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert 'recipes' in data
    assert 'total_results' in data
    assert isinstance(data['recipes'], list)

def test_get_recipes_missing_query(client):
    response = client.get('/api/recipes')
    assert response.status_code == 400
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert 'error' in data
    assert 'Search query required' in data['error']

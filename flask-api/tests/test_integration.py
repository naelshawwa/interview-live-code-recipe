#!/usr/bin/env python3
"""
Test script for the Spoonacular API integration.
This script demonstrates how the API endpoint works with and without credentials.
"""

import sys
import os
# Add the parent directory to the path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import create_app
import json

def test_api_integration():
    app = create_app()
    
    print("Testing Spoonacular API Integration")
    print("=" * 50)
    
    with app.test_client() as client:
        print("\n1. Testing without search query:")
        response = client.get('/api/recipes')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.get_json(), indent=2)}")
        
        print("\n2. Testing with search query but no credentials:")
        response = client.get('/api/recipes?q=chicken')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.get_json(), indent=2)}")
        
        print("\n3. API Endpoint Documentation:")
        print("   URL: /api/recipes")
        print("   Method: GET")
        print("   Required Parameter: q (search query)")
        print("   Example: /api/recipes?q=chicken")
        print("   Required Environment Variables:")
        print("     - SPOONACULAR_API_KEY: Your Spoonacular API Key")
        print("\n   To get your API key:")
        print("   Visit: https://spoonacular.com/food-api/console#Dashboard")

if __name__ == "__main__":
    test_api_integration()
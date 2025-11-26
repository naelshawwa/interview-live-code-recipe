import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .routes.recipes import register_routes

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configure app with environment variables
    app.config['SPOONACULAR_API_KEY'] = os.getenv('SPOONACULAR_API_KEY')
    
    # Enable CORS for all routes
    CORS(app)

    # Register routes
    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
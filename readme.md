# Full Stack Engineering Interview

We're building yet another recipe website using the [Spoonacular API](https://spoonacular.com/food-api/). 

Before the interview:
- Checkout this project
- Signup for a free account for Spoonacular and get your api key
- Save your api key in an enviroment variable for `SPOONACULAR_API_KEY` here:
   
   ```/flask-api/.env```

- install NPM and Poetry dependencies and start the application and ensure you are able to see recipes
- DO NOT MAKE ANY CHANGES to this codebase before the interview however feel free to browse the [Spoonacular API Docs](https://spoonacular.com/food-api/docs) and this codebase.

# Codebase
This interview codebase has 3 parts. For Engineering roles we will be using both the ReactJS and Python Flask parts. For Test Engineer roles we will be using the Playwright codebase as well as the unit tests for ReactJS Client or Python Flask API depending 

## ReactJS Client

##  Python Flask API
### Overview
This project is a Flask API that serves as a backend for applications. It is structured to facilitate easy development and testing of API endpoints.

### Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-api
   ```

2. **Install Poetry:**
   Follow the instructions at [Poetry's official website](https://python-poetry.org/docs/#installation) to install Poetry.

3. **Install dependencies:**
   ```
   poetry install
   ```

4. **Run the application:**
   ```
   poetry run python -m src.app
   ```
5. **Run tests:**
   ```
   poetry run pytest -v
   ```


### Testing
To run the tests, use the following command:
```
poetry run pytest tests/test_app.py
```

## Playwright Tests
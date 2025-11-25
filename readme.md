# Full Stack Engineering Interview

We're building yet another recipe website using the [Edamam API](https://developer.edamam.com/edamam-docs-recipe-api). 

Before the interview:
- checkout this project
- sign up for a free developer account on Edamam to get your API key
- install dependencies and start the application and ensure you are able to see recipes
- DO NOT MAKE ANY CHANGES to this codebase before the interview however feel free to 

# Codebase
This interview codebase has 3 parts. For Engineering roles we will be using both the ReactJS and Python Flask parts. For Test Engineer roles we will be using the Playwright codebase as well as the unit tests for ReactJS Client or Python Flask API

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
   poetry run python src/app.py
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
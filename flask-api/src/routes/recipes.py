from flask import jsonify, request, current_app
from http import HTTPStatus
import requests
import logging
from ..models.recipe import Recipe

logger = logging.getLogger(__name__)

def register_routes(app):
    @app.route('/api/recipes', methods=['GET'])
    def get_recipes():
        api_key = current_app.config.get('SPOONACULAR_API_KEY')
        
        if not api_key:
            return jsonify({
                'error': 'API credentials not configured',
                'message': 'Please set SPOONACULAR_API_KEY environment variable'
            }), HTTPStatus.INTERNAL_SERVER_ERROR
        
        query = request.args.get('q', '').strip()
        
        if not query:
            return jsonify({
                'error': 'Search query required',
                'message': 'Please provide a search query using the "q" parameter'
            }), HTTPStatus.BAD_REQUEST
        
        try:
            spoonacular_url = 'https://api.spoonacular.com/recipes/complexSearch'
            params = {
                'apiKey': api_key,
                'query': query,
                'number': 3,       
                'sort': 'popularity'
            }
            
            response = requests.get(spoonacular_url, params=params, timeout=10)
            response.raise_for_status()
            
            api_data = response.json()
            
            recipes = []
            if 'results' in api_data:
                for recipe_data in api_data['results']:
                    
                    recipe = Recipe.from_spoonacular_data(recipe_data)
                    recipes.append(recipe.model_dump())
            
            return jsonify({
                'recipes': recipes,
                'total_results': api_data.get('totalResults', 0)
            }), HTTPStatus.OK
            
        except requests.exceptions.Timeout:
            logger.error('Spoonacular API request timed out')
            return jsonify({
                'error': 'Request timeout',
                'message': 'The recipe search request timed out. Please try again.'
            }), HTTPStatus.REQUEST_TIMEOUT
            
        except requests.exceptions.HTTPError as e:
            logger.error(f'Spoonacular API HTTP error: {e}')
            # Extract status code from response or exception
            status_code = getattr(e.response, 'status_code', None) or 500
            
            # Try to extract detailed error message from API response
            api_error_message = ''
            if e.response:
                try:
                    error_data = e.response.json()
                    if 'message' in error_data:
                        api_error_message = f" API message: {error_data['message']}"
                    elif 'error' in error_data:
                        api_error_message = f" API error: {error_data['error']}"
                except:
                    # If we can't parse JSON, use the raw text
                    api_error_message = f" Response: {e.response.text[:200]}..."
            
            if status_code == 401:
                return jsonify({
                    'error': 'Authentication failed',
                    'message': f'Invalid API credentials. Please check your SPOONACULAR_API_KEY.{api_error_message}',
                    'debug_info': {
                        'status_code': status_code,
                        'exception': str(e),
                        'url': e.response.url if e.response else None
                    }
                }), HTTPStatus.UNAUTHORIZED
            elif status_code == 403:
                return jsonify({
                    'error': 'Access forbidden',
                    'message': f'Access to the Spoonacular API was denied. Please check your subscription.{api_error_message}'
                }), HTTPStatus.FORBIDDEN
            elif status_code == 402:
                return jsonify({
                    'error': 'Quota exceeded',
                    'message': f'Your Spoonacular API quota has been exceeded. Please upgrade your plan.{api_error_message}'
                }), HTTPStatus.PAYMENT_REQUIRED
            else:
                return jsonify({
                    'error': 'API request failed',
                    'message': f'Spoonacular API returned an error: {status_code}.{api_error_message}'
                }), HTTPStatus.BAD_GATEWAY
                
        except requests.exceptions.RequestException as e:
            logger.error(f'Spoonacular API request failed: {e}')
            return jsonify({
                'error': 'API request failed',
                'message': f'Failed to connect to the recipe search service. Error: {str(e)}',
                'debug_info': {
                    'exception_type': type(e).__name__,
                    'exception_message': str(e)
                }
            }), HTTPStatus.SERVICE_UNAVAILABLE
            
        except Exception as e:
            logger.error(f'Unexpected error in recipe search: {e}')
            return jsonify({
                'error': 'Internal server error',
                'message': f'An unexpected error occurred while searching for recipes: {str(e)}',
                'debug_info': {
                    'exception_type': type(e).__name__,
                    'exception_message': str(e)
                }
            }), HTTPStatus.INTERNAL_SERVER_ERROR
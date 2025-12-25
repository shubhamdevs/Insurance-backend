from functools import wraps
from flask import request, jsonify
from config import get_config
from datetime import datetime
import logging

config = get_config()
logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# API Key Validation Decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        
        if not api_key:
            logger.warning("Request received without API key")
            return jsonify({
                'status': 'error',
                'message': 'API Key is required',
                'code': 'MISSING_API_KEY'
            }), 401
        
        if api_key != config.API_KEY:
            logger.warning(f"Invalid API key attempt: {api_key}")
            return jsonify({
                'status': 'error',
                'message': 'Invalid API Key',
                'code': 'INVALID_API_KEY'
            }), 403
        
        return f(*args, **kwargs)
    return decorated_function

# Error Handler
def error_response(message, code, status_code=400):
    return jsonify({
        'status': 'error',
        'message': message,
        'code': code,
        'timestamp': datetime.utcnow().isoformat()
    }), status_code

# Success Response
def success_response(data, message='Success', status_code=200):
    return jsonify({
        'status': 'success',
        'message': message,
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    }), status_code

# Validate Input
def validate_required_fields(data, required_fields):
    missing = [field for field in required_fields if field not in data or data[field] is None]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    return True, None

from flask import Flask, request, jsonify
from flask_cors import CORS
from config import get_config
from utils import require_api_key, success_response, error_response, validate_required_fields
from models import PolicyHolder, RealTimeData
import logging

# Initialize Flask app
app = Flask(__name__)
config = get_config()

# Load configuration
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['JSON_SORT_KEYS'] = False

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure logging
logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# ============================================================================
# ROOT ENDPOINT
# ============================================================================

@app.route('/', methods=['GET'])
def root():
    """Root endpoint - API information"""
    return success_response({
        'service': 'Insurance API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'health': '/health',
            'policy_status': '/api/v1/policy/status',
            'claims_balance': '/api/v1/policy/claims-balance',
            'premium_info': '/api/v1/policy/premium',
            'coverage_details': '/api/v1/policy/coverage',
            'beneficiaries': '/api/v1/policy/beneficiaries',
            'medical_history': '/api/v1/policy/medical-history',
            'complete_info': '/api/v1/policy/complete-info'
        },
        'note': 'All /api/v1/* endpoints require X-API-Key header'
    }, 'Insurance API is running')

# ============================================================================
# HEALTH CHECK ENDPOINT
# ============================================================================

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint - no API key required"""
    return success_response({
        'service': 'Insurance API',
        'status': 'healthy',
        'version': '1.0.0'
    }, 'Health check passed')

# ============================================================================
# POLICY ENDPOINTS
# ============================================================================

@app.route('/api/v1/policy/status', methods=['POST'])
@require_api_key
def get_policy_status():
    """
    Get real-time policy status
    Request body: { "policy_id": "SH-2024-987654" }
    """
    try:
        data = request.get_json()
        
        # Validate input
        is_valid, error_msg = validate_required_fields(data, ['policy_id'])
        if not is_valid:
            return error_response(error_msg, 'VALIDATION_ERROR', 400)
        
        policy_id = data['policy_id']
        logger.info(f"Fetching policy status for {policy_id}")
        
        # Get real-time data
        status = RealTimeData.get_policy_status(policy_id)
        
        return success_response(status, 'Policy status retrieved successfully')
    
    except Exception as e:
        logger.error(f"Error in get_policy_status: {str(e)}")
        return error_response('Internal server error', 'INTERNAL_ERROR', 500)

@app.route('/api/v1/policy/claims-balance', methods=['POST'])
@require_api_key
def get_claims_balance():
    """
    Get real-time claims balance information
    Request body: { "policy_id": "SH-2024-987654" }
    """
    try:
        data = request.get_json()
        
        is_valid, error_msg = validate_required_fields(data, ['policy_id'])
        if not is_valid:
            return error_response(error_msg, 'VALIDATION_ERROR', 400)
        
        policy_id = data['policy_id']
        logger.info(f"Fetching claims balance for {policy_id}")
        
        claims = RealTimeData.get_claims_balance(policy_id)
        
        return success_response(claims, 'Claims balance retrieved successfully')
    
    except Exception as e:
        logger.error(f"Error in get_claims_balance: {str(e)}")
        return error_response('Internal server error', 'INTERNAL_ERROR', 500)

@app.route('/api/v1/policy/premium', methods=['POST'])
@require_api_key
def get_premium_info():
    """
    Get real-time premium payment information
    Request body: { "policy_id": "SH-2024-987654" }
    """
    try:
        data = request.get_json()
        
        is_valid, error_msg = validate_required_fields(data, ['policy_id'])
        if not is_valid:
            return error_response(error_msg, 'VALIDATION_ERROR', 400)
        
        policy_id = data['policy_id']
        logger.info(f"Fetching premium info for {policy_id}")
        
        premium = RealTimeData.get_premium_info(policy_id)
        
        return success_response(premium, 'Premium information retrieved successfully')
    
    except Exception as e:
        logger.error(f"Error in get_premium_info: {str(e)}")
        return error_response('Internal server error', 'INTERNAL_ERROR', 500)

@app.route('/api/v1/policy/coverage', methods=['POST'])
@require_api_key
def get_coverage_details():
    """
    Get real-time coverage details (per coverage type usage)
    Request body: { "policy_id": "SH-2024-987654" }
    """
    try:
        data = request.get_json()
        
        is_valid, error_msg = validate_required_fields(data, ['policy_id'])
        if not is_valid:
            return error_response(error_msg, 'VALIDATION_ERROR', 400)
        
        policy_id = data['policy_id']
        logger.info(f"Fetching coverage details for {policy_id}")
        
        coverage = RealTimeData.get_coverage_details(policy_id)
        
        return success_response(coverage, 'Coverage details retrieved successfully')
    
    except Exception as e:
        logger.error(f"Error in get_coverage_details: {str(e)}")
        return error_response('Internal server error', 'INTERNAL_ERROR', 500)

# ============================================================================
# BENEFICIARY ENDPOINTS
# ============================================================================

@app.route('/api/v1/policy/beneficiaries', methods=['POST'])
@require_api_key
def get_beneficiaries():
    """
    Get beneficiary information
    Request body: { "policy_id": "SH-2024-987654" }
    """
    try:
        data = request.get_json()
        
        is_valid, error_msg = validate_required_fields(data, ['policy_id'])
        if not is_valid:
            return error_response(error_msg, 'VALIDATION_ERROR', 400)
        
        policy_id = data['policy_id']
        logger.info(f"Fetching beneficiaries for {policy_id}")
        
        beneficiaries = RealTimeData.get_beneficiary_info(policy_id)
        
        return success_response(beneficiaries, 'Beneficiary information retrieved successfully')
    
    except Exception as e:
        logger.error(f"Error in get_beneficiaries: {str(e)}")
        return error_response('Internal server error', 'INTERNAL_ERROR', 500)

# ============================================================================
# MEDICAL HISTORY ENDPOINTS
# ============================================================================

@app.route('/api/v1/policy/medical-history', methods=['POST'])
@require_api_key
def get_medical_history():
    """
    Get medical history and health information
    Request body: { "policy_id": "SH-2024-987654" }
    """
    try:
        data = request.get_json()
        
        is_valid, error_msg = validate_required_fields(data, ['policy_id'])
        if not is_valid:
            return error_response(error_msg, 'VALIDATION_ERROR', 400)
        
        policy_id = data['policy_id']
        logger.info(f"Fetching medical history for {policy_id}")
        
        medical = RealTimeData.get_medical_history(policy_id)
        
        return success_response(medical, 'Medical history retrieved successfully')
    
    except Exception as e:
        logger.error(f"Error in get_medical_history: {str(e)}")
        return error_response('Internal server error', 'INTERNAL_ERROR', 500)

# ============================================================================
# COMPOSITE ENDPOINT (Get All Info at Once)
# ============================================================================

@app.route('/api/v1/policy/complete-info', methods=['POST'])
@require_api_key
def get_complete_policy_info():
    """
    Get all policy information in one call
    Request body: { "policy_id": "SH-2024-987654" }
    """
    try:
        data = request.get_json()
        
        is_valid, error_msg = validate_required_fields(data, ['policy_id'])
        if not is_valid:
            return error_response(error_msg, 'VALIDATION_ERROR', 400)
        
        policy_id = data['policy_id']
        logger.info(f"Fetching complete policy info for {policy_id}")
        
        # Combine all real-time data
        complete_info = {
            'policy_id': policy_id,
            'status': RealTimeData.get_policy_status(policy_id),
            'claims': RealTimeData.get_claims_balance(policy_id),
            'premium': RealTimeData.get_premium_info(policy_id),
            'coverage': RealTimeData.get_coverage_details(policy_id),
            'beneficiaries': RealTimeData.get_beneficiary_info(policy_id),
            'medical_history': RealTimeData.get_medical_history(policy_id)
        }
        
        return success_response(complete_info, 'Complete policy information retrieved successfully')
    
    except Exception as e:
        logger.error(f"Error in get_complete_policy_info: {str(e)}")
        return error_response('Internal server error', 'INTERNAL_ERROR', 500)

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return error_response('Endpoint not found', 'NOT_FOUND', 404)

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return error_response('Internal server error', 'INTERNAL_ERROR', 500)

# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == '__main__':
    logger.info(f"Starting Insurance API on {config.API_HOST}:{config.API_PORT}")
    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.FLASK_DEBUG)
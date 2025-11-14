"""Health check controller."""
from flask import Blueprint


healthcheck_bp = Blueprint('healthcheck', __name__)


@healthcheck_bp.route('/ping', methods=['GET'])
def ping():
    """
    Health check endpoint.
    
    Returns:
        Simple pong response with 200 status
    """
    return "pong", 200


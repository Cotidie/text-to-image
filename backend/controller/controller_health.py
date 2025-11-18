from flask import Blueprint

healthcheck_blueprint = Blueprint('healthcheck', __name__)

@healthcheck_blueprint.route("/ping", methods=["GET"])
def ping():
    """
    Health check endpoint.
    
    Returns:
        Simple pong response with 200 status
    """
    return "pong", 200

@healthcheck_blueprint.route("/info", methods=["GET"])
def info():
    """
    Information endpoint.
    
    Returns:
        Basic information about the service
    """
    return {
        "service": "Text-to-Image Generation Server",
        "status": "running"
    }, 200
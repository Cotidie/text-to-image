"""Health check controller."""
from flask import Blueprint
from endpoint import PING


healthcheck_blueprint = Blueprint('healthcheck', __name__)


@healthcheck_blueprint.route(PING.path, methods=PING.methods())
def ping():
    """
    Health check endpoint.
    
    Returns:
        Simple pong response with 200 status
    """
    return "pong", 200


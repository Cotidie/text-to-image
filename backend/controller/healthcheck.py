"""Health check controller."""


def ping():
    """
    Health check endpoint.
    
    Returns:
        Simple pong response with 200 status
    """
    return "pong", 200

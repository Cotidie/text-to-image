from flask.views import MethodView

class PingAPI(MethodView):
    """Handle ping requests to check server health."""

    def get(self):
        """Respond to GET requests with a simple 'pong' message."""
        return "pong", 200
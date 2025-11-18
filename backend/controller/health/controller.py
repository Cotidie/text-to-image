from flask import Blueprint
from .ping import PingAPI

class HealthController:
    """Controller for health check endpoints."""

    PREFIX = "/health"

    def __init__(self):
        self.api_ping = PingAPI()

        self.blueprint = Blueprint('healthcheck', __name__, url_prefix=self.PREFIX)
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule(
            '/ping', 
            view_func=self.api_ping.as_view('/health/ping'), 
            methods=['GET']
        )

    def get_blueprint(self):
        return self.blueprint

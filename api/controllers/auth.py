from django.core.exceptions import BadRequest
from rest_framework.exceptions import NotFound

from api.controllers.provider import ProviderController


class OAuth2Controller:
    def __init__(self):
        self.provider_controller = ProviderController()

    def get_auth_code(self, provider):
        try:
            provider = self.provider_controller.find_by_name(provider)
        except NotFound:
            raise BadRequest





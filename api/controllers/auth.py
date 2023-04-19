from django.core.exceptions import BadRequest
from rest_framework.exceptions import NotFound

from api.controllers.provider import ProviderController


class OAuth2Controller:
    def __init__(self):
        self.provider_controller = ProviderController()

    def get_auth_code(self,
                      client_id,
                      scopes,
                      redirect_uri,
                      state=None):

        if client_id is None:
            raise BadRequest

        provider = None
        try:
            provider = self.provider_controller.find_by_client_id(client_id)
        except NotFound:
            pass

        if provider is None:
            raise BadRequest

        # Verify credentials











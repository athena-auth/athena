from django.core.exceptions import BadRequest
from rest_framework.exceptions import NotFound
from api.controllers.provider import ProviderController
from urllib import parse


class OAuth2Controller:
    def __init__(self):
        self.provider_controller = ProviderController()

    # def get_auth_url(self,
    #                  client_id,
    #                  scopes,
    #                  redirect_uri,
    #                  state=None):
    #     if client_id is None:
    #         raise BadRequest
    #
    #     if scopes is None:
    #         raise BadRequest
    #
    #     if redirect_uri is None:
    #         raise BadRequest
    #
    #     provider = None
    #     try:
    #         provider = self.provider_controller.find_by_client_id(client_id)
    #     except NotFound:
    #         pass
    #
    #     if provider is None:
    #         raise BadRequest
    #
    #     scopes_array = scopes.split(".")
    #     if scopes_array is None:
    #         raise BadRequest
    #
    #     for scope in scopes_array:
    #         if scope not in provider.scopes:
    #             raise BadRequest
    #
    #     if redirect_uri not in provider.redirect_uris:
    #         raise BadRequest
    #
    #     # TODO: Make this a format in the db, instead of hardcoded endpoint
    #     auth_code_params = {
    #         "client_id": client_id, "state": state, "redirect_uri": redirect_uri,
    #         "scope": scopes, "response_type": "code"
    #     }
    #
    #     auth_url = f"{provider.code_endpoint}?{parse.urlencode(auth_code_params)}"
    #
    #     return auth_url

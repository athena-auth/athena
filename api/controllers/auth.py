from urllib.parse import urlencode

from api.controllers.provider import ProviderController
from api.models import Endpoint
from api.utils.constants import STATE_PARAM, RESPONSE_TYPE_PARAM, ORIGIN_HEADER, GRANT_TYPE
import requests


class AuthorizationController:
    def __init__(self):
        self.provider_controller = ProviderController()

    def authorize_provider(self, request, provider_name):
        provider = self.provider_controller.find_by_name(name=provider_name)

        if provider is None:
            return None

        state = request.GET.get(STATE_PARAM)
        if state is not None:
            state = state.rstrip("/")

        # Build the authorization url based on RFC6749 spec
        client_id = provider.client_id
        redirect_uri = provider.redirect_uri
        scope = provider.scope

        # Build the delimited scope
        if scope is not None:
            delimiter = scope.get_delimiter()
            scope = delimiter.join(scope.values)

        authorize_endpoint = provider.endpoints.filter(type=Endpoint.EndpointType.CODE).first()

        if authorize_endpoint is None:
            return None

        parameters = dict()
        parameters["response_type"] = RESPONSE_TYPE_PARAM
        parameters["client_id"] = client_id

        if redirect_uri is not None:
            parameters["redirect_uri"] = redirect_uri

        if scope is not None:
            parameters["scope"] = scope

        if state is not None:
            parameters["state"] = state

        additional_params = authorize_endpoint.parameters.all()
        if additional_params is not None and len(additional_params) != 0:
            for additional_param in additional_params:
                parameters[additional_param.name] = additional_param.value

        authorize_endpoint = f"{authorize_endpoint.base_url}?{urlencode(parameters)}"

        return authorize_endpoint

    def authenticate_provider(self, request, provider_name):
        provider = self.provider_controller.find_by_name(provider_name)

        if provider is None:
            return None

        redirect_uri = request.headers.get(ORIGIN_HEADER)
        if redirect_uri is None:
            return None

        code = request.data.get("code")
        if code is None:
            return None

        client_id = provider.client_id
        client_secret = provider.client_secret

        authenticate_endpoint = provider.endpoints.filter(type=Endpoint.EndpointType.TOKEN).first()
        if authenticate_endpoint is None:
            return None

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body = {
            "grant_type": GRANT_TYPE,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "code": code
        }

        authenticate_request = requests.post(authenticate_endpoint.base_url, data=body, headers=headers)

        if authenticate_request.status_code != 200:
            return None

        return authenticate_request.json()



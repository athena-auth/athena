from urllib.parse import urlencode

from api.controllers.provider import ProviderController
from api.models import Endpoint
from api.utils.constants import STATE_PARAM, RESPONSE_TYPE_PARAM


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
        if client_id is None:
            return None

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

    def persist_session(self):
        # TODO: create a new user session
        # Such sessions are created once the user successfully has access to a protected resource
        pass



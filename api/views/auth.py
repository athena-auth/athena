from django.core.exceptions import BadRequest
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from api.controllers.auth import OAuth2Controller
from api.utils.constants import STATE_PARAM, REDIRECT_URI_PARAM, SCOPES_PARAM


class OAuth2View(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = OAuth2Controller()

    def get(self, request, client_id):
        try:
            scopes = request.query_params.get(SCOPES_PARAM)
            redirect_uri = request.query_params.get(REDIRECT_URI_PARAM)
            state = request.query_params.get(STATE_PARAM)

            self.controller.get_auth_code(client_id, scopes, redirect_uri, state)
            return Response({"provider": client_id}, status=HTTP_200_OK)
        except BadRequest:
            return Response(status=HTTP_400_BAD_REQUEST)

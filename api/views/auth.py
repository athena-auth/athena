from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from api.controllers.auth import AuthorizationController


class AuthorizationView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = AuthorizationController()

    def get(self, request, name):
        if name is None:
            return Response(status=HTTP_400_BAD_REQUEST)

        authorization_url = self.controller.authorize_provider(request=request, provider_name=name)

        if authorization_url is None:
            return Response(status=HTTP_400_BAD_REQUEST)

        return Response({"authorization_url": authorization_url}, status=HTTP_200_OK)


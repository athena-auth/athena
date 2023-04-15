from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from api.controllers.auth import OAuth2Controller


class OAuth2View(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = OAuth2Controller()

    def get(self, request, provider):
        self.controller.get_auth_code(provider)

        return Response({"provider": provider}, status=HTTP_200_OK)

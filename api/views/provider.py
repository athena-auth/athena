from django.core.exceptions import BadRequest
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_204_NO_CONTENT)
from rest_framework.views import APIView
from api.controllers.provider import ProviderController


class ProvidersView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = ProviderController()

    def get(self, request):
        serializer = self.controller.get_providers()
        return Response(serializer.data, status=HTTP_200_OK)


class ProviderView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = ProviderController()

    def get(self, request, key):
        try:
            serializer = self.controller.get_provider(key=key)
            return Response(serializer.data, status=HTTP_200_OK)
        except NotFound:
            return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request, client_id=None):
        provider = None
        if client_id is None:
            provider = self.controller.create_provider(request=request)
        else:
            provider = self.controller.update_provider(client_id=client_id, request=request)

        if provider is None or provider.data is None:
            return Response(status=HTTP_400_BAD_REQUEST)

        return Response(provider.data, status=HTTP_200_OK)


    def delete(self, request, key):
        try:
            self.controller.delete_provider(key=key)
            return Response(status=HTTP_204_NO_CONTENT)
        except BadRequest:
            return Response(status=HTTP_400_BAD_REQUEST)

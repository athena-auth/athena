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

    def post(self, request, key=None):
        if key is not None:
            serializer = self.controller.update_provider(key=key, request=request)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            try:
                serializer = self.controller.create_provider(request=request)
                return Response(serializer.data, status=HTTP_201_CREATED)
            except BadRequest:
                return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, key):
        try:
            self.controller.delete_provider(key=key)
            return Response(status=HTTP_204_NO_CONTENT)
        except BadRequest:
            return Response(status=HTTP_400_BAD_REQUEST)

from django.core.exceptions import BadRequest
from rest_framework.exceptions import NotFound

from api.models import Provider
from api.serializers import ProviderSerializer


class ProviderController:

    def get_providers(self):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return serializer

    def get_provider(self, key):
        provider = None
        try:
            provider = Provider.objects.get(pk=key)
        except Provider.DoesNotExist:
            pass

        if provider is None:
            raise NotFound

        serializer = ProviderSerializer(provider)
        return serializer

    def create_provider(self, request):
        serializer = ProviderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return serializer
        else:
            raise BadRequest


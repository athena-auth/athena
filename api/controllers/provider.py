from rest_framework.exceptions import NotFound
from api.models import Provider
from api.serializers.provider import ProviderSerializer


class ProviderController:

    def find_by_client_id(self, client_id):
        if client_id is None:
            return None

        provider = None
        try:
            provider = Provider.objects.get(client_id=client_id)
        except Provider.DoesNotExist:
            return None

        return provider

    def find_by_key(self, key):
        provider = None
        try:
            provider = Provider.objects.get(pk=key)
        except Provider.DoesNotExist:
            pass

        if provider is None:
            raise NotFound

        return provider

    def get_providers(self):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return serializer

    def get_provider(self, key):
        provider = self.find_by_key(key)

        serializer = ProviderSerializer(provider)
        return serializer

    def create_provider(self, request):
        if request is None or request.data is None:
            return None

        provider_serializer = ProviderSerializer(data=request.data)
        if not provider_serializer.is_valid():
            return None

        provider_serializer.save()

        return provider_serializer

    def update_provider(self, client_id, request):
        provider = self.find_by_client_id(client_id)

        if provider is None:
            return None

        provider_serializer = ProviderSerializer(instance=provider, data=request.data, partial=True)
        if not provider_serializer.is_valid():
            return None

        provider_serializer.save()

        return provider_serializer

    def delete_provider(self, key):
        provider = self.find_by_key(key=key)
        provider.delete()

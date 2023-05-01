from rest_framework.serializers import ModelSerializer
from api.models import Endpoint
from api.models.provider import Provider
from api.serializers.endpoint import EndpointSerializer


class ProviderSerializer(ModelSerializer):
    endpoints = EndpointSerializer(allow_null=False, many=True)

    class Meta:
        model = Provider
        fields = ["name", "client_id", "client_secret", "redirect_uri", "scope", "public_key", "endpoints", "disabled"]

    def create(self, validated_data):
        name = validated_data.get("name")
        client_id = validated_data.get("client_id")
        client_secret = validated_data.get("client_secret")
        redirect_uri = validated_data.get("redirect_uri")
        scope = validated_data.get("scope")
        public_key = validated_data.get("public_key")

        provider = Provider.objects.create(name=name,
                                           disabled=False,
                                           client_id=client_id,
                                           client_secret=client_secret,
                                           scope=scope,
                                           redirect_uri=redirect_uri,
                                           public_key=public_key)

        endpoints = validated_data.get("endpoints")
        if len(endpoints) == 0:
            return None

        for endpoint in endpoints:
            endpoint_serializer = EndpointSerializer(data=endpoint)
            if not endpoint_serializer.is_valid():
                return None

            endpoint_serializer.save(provider=provider)

            if endpoint_serializer is None or endpoint_serializer.data is None:
                return None

        return provider

    def update(self, instance, validated_data):
        endpoints = []
        if validated_data.get("endpoints") is not None:
            endpoints = validated_data.pop("endpoints")

        provider = super().update(instance=instance, validated_data=validated_data)

        if len(endpoints) == 0:
            return None

        touched_endpoints = []
        for endpoint in endpoints:
            endpoint_id = endpoint.get("id")
            if endpoint_id is None:
                endpoint_serializer = EndpointSerializer(data=endpoint)

                if not endpoint_serializer.is_valid():
                    return None

                endpoint_serializer.save(provider=provider)

                if endpoint_serializer is None or endpoint_serializer.data is None:
                    return None

                touched_endpoints.append(endpoint_serializer.data.get("id"))

            else:
                endpoint_instance = None
                try:
                    endpoint_instance = Endpoint.objects.get(pk=endpoint_id)
                except Endpoint.DoesNotExist:
                    return None

                endpoint_serializer = EndpointSerializer(instance=endpoint_instance, data=endpoint, partial=True)

                if not endpoint_serializer.is_valid():
                    return None

                endpoint_serializer.save()

                if endpoint_serializer is None or endpoint_serializer.data is None:
                    return None

                touched_endpoints.append(endpoint_id)

        # Remove endpoints
        current_endpoints = [endpoint for endpoint in instance.endpoints.all()]
        for current_endpoint in current_endpoints:
            if current_endpoint.id not in touched_endpoints:
                current_endpoint.delete()

        return provider

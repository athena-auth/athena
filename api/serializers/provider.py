from django.core.exceptions import BadRequest
from rest_framework.serializers import ModelSerializer

from api.models import Endpoint
from api.models.provider import Provider
from api.serializers.endpoint import EndpointSerializer


class ProviderSerializer(ModelSerializer):
    endpoints = EndpointSerializer(many=True)

    class Meta:
        model = Provider
        fields = '__all__'

    def create(self, validated_data):
        provider = Provider.objects.create(name=validated_data["name"],
                                           description=validated_data["description"]
                                           if "description" in validated_data else None,
                                           disabled=False)

        endpoint_data = validated_data["endpoints"]
        if endpoint_data is None or len(endpoint_data) == 0:
            raise BadRequest

        for endpoint in endpoint_data:
            endpoint_serializer = EndpointSerializer(data=endpoint)
            if endpoint_serializer.is_valid():
                endpoint_serializer.save(provider=provider)
            else:
                raise BadRequest

        return provider

    def update(self, instance, validated_data):
        endpoint_data = None

        if "endpoints" in validated_data:
            endpoint_data = validated_data.pop("endpoints")

        provider = super().update(instance=instance, validated_data=validated_data)

        if endpoint_data is not None and len(endpoint_data) == 0:
            raise BadRequest

        if endpoint_data is not None:
            created_or_updated_endpoint_ids = []

            for endpoint in endpoint_data:
                if endpoint["id"] is None:
                    endpoint_serializer = EndpointSerializer(data=endpoint)

                    if endpoint_serializer.is_valid():
                        endpoint_serializer.save(provider=provider)
                        created_or_updated_endpoint_ids.append(endpoint_serializer.data.get("id"))
                    else:
                        raise BadRequest
                else:
                    try:
                        found_endpoint = Endpoint.objects.get(pk=endpoint["id"])
                        endpoint_serializer = EndpointSerializer(found_endpoint, data=endpoint, partial=True)

                        if endpoint_serializer.is_valid():
                            endpoint_serializer.save()
                            created_or_updated_endpoint_ids.append(endpoint_serializer.data.get("id"))
                        else:
                            raise BadRequest
                    except Endpoint.DoesNotExist:
                        raise BadRequest

            current_endpoints = [endpoint for endpoint in instance.endpoints.all()]
            for current_endpoint in current_endpoints:
                if current_endpoint.id not in created_or_updated_endpoint_ids:
                    current_endpoint.delete()

        return provider

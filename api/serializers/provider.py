from django.core.exceptions import BadRequest
from rest_framework.serializers import ModelSerializer
from api.models.provider import Provider
from api.serializers.endpoint import EndpointSerializer


class ProviderSerializer(ModelSerializer):
    endpoints = EndpointSerializer(many=True)

    class Meta:
        model = Provider
        fields = '__all__'

    def create(self, validated_data):
        provider = Provider.objects.create(name=validated_data["name"],
                                           description=validated_data["description"],
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



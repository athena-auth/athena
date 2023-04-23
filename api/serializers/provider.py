from django.core.exceptions import BadRequest
from rest_framework.serializers import ModelSerializer

from api.models import Endpoint, Parameter
from api.models.provider import Provider
from api.serializers.endpoint import EndpointSerializer


class ProviderSerializer(ModelSerializer):
    endpoints = EndpointSerializer(many=True)

    class Meta:
        model = Provider
        fields = '__all__'

    def create(self, validated_data):
        endpoints = validated_data.pop("endpoints")

        provider = Provider(**validated_data)
        provider.save()

        for e in endpoints:
            parameters = e.pop("parameters")

            if parameters is None or len(parameters) == 0:
                raise BadRequest

            endpoint = Endpoint(**e, provider=provider)
            endpoint.save()

            for p in parameters:
                parameter = Parameter(**p, endpoint=endpoint)
                parameter.save()

        return provider

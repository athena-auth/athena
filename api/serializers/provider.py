from rest_framework.serializers import ModelSerializer
from api.models.provider import Provider
from api.serializers.endpoint import EndpointSerializer


class ProviderSerializer(ModelSerializer):
    endpoints = EndpointSerializer(many=True)

    class Meta:
        model = Provider
        fields = '__all__'

from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from api.models import Endpoint
from api.serializers.parameter import ParameterSerializer


class EndpointSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    parameters = ParameterSerializer(many=True)

    class Meta:
        model = Endpoint
        fields = ["id", "type", "http_method", "base_url", "parameters"]

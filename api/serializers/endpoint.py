from rest_framework.serializers import ModelSerializer
from api.models import Endpoint
from api.serializers.parameter import ParameterSerializer


class EndpointSerializer(ModelSerializer):
    parameters = ParameterSerializer(many=True)

    class Meta:
        model = Endpoint
        fields = '__all__'

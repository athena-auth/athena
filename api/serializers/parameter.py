from rest_framework.serializers import ModelSerializer

from api.models import Parameter


class ParameterSerializer(ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'

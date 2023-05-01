from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from api.models import Parameter


class ParameterSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = Parameter
        fields = ["id", "name", "value"]

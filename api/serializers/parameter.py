from django.core.exceptions import BadRequest
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from api.models import Parameter


class ParameterSerializer(ModelSerializer):
    id = IntegerField(allow_null=True)

    class Meta:
        model = Parameter
        fields = ["id", "name", "value"]

    def create(self, validated_data):
        endpoint = validated_data["endpoint"]
        if endpoint is None:
            raise BadRequest

        parameter = Parameter.objects.create(endpoint=endpoint,
                                             name=validated_data["name"],
                                             value=validated_data["value"])
        return parameter

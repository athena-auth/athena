from django.core.exceptions import BadRequest
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from api.models import Endpoint, Parameter
from api.serializers.parameter import ParameterSerializer


class EndpointSerializer(ModelSerializer):
    id = IntegerField(allow_null=True)
    parameters = ParameterSerializer(many=True)

    class Meta:
        model = Endpoint
        fields = ["id", "type", "http_method", "base_url", "parameters"]

    def create(self, validated_data):
        provider = validated_data["provider"]
        if provider is None:
            raise BadRequest

        endpoint = Endpoint.objects.create(provider=provider,
                                           type=validated_data["type"],
                                           http_method=validated_data["http_method"],
                                           base_url=validated_data["base_url"])

        parameter_data = validated_data["parameters"]
        if parameter_data is None or len(parameter_data) == 0:
            raise BadRequest

        for parameter in parameter_data:
            parameter_serializer = ParameterSerializer(data=parameter)
            if parameter_serializer.is_valid():
                parameter_serializer.save(endpoint=endpoint)
            else:
                raise BadRequest

        return endpoint

    def update(self, instance, validated_data):
        parameter_data = validated_data.pop("parameters")

        endpoint = super().update(instance, validated_data)

        if parameter_data is None or len(parameter_data) == 0:
            raise BadRequest

        for parameter in parameter_data:
            if parameter["id"] is None:
                parameter_serializer = ParameterSerializer(data=parameter)

                if parameter_serializer.is_valid():
                    parameter_serializer.save(endpoint=endpoint)
                else:
                    raise BadRequest
            else:
                try:
                    found_parameter = Parameter.objects.get(pk=parameter["id"])
                    parameter_serializer = ParameterSerializer(found_parameter, data=parameter, partial=True)

                    if parameter_serializer.is_valid():
                        parameter_serializer.save()
                    else:
                        raise BadRequest
                except Parameter.DoesNotExist:
                    raise BadRequest

        return endpoint


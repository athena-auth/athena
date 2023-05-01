from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from api.models import Endpoint, Parameter
from api.serializers.parameter import ParameterSerializer


class EndpointSerializer(ModelSerializer):
    id = IntegerField(required=False)
    parameters = ParameterSerializer(allow_null=True, many=True)

    class Meta:
        model = Endpoint
        fields = ["id", "type", "base_url", "parameters"]

    def create(self, validated_data):
        provider = validated_data.get("provider")
        if provider is None:
            return None

        endpoint_type = validated_data.get("type")
        base_url = validated_data.get("base_url")

        endpoint = Endpoint.objects.create(provider=provider, type=endpoint_type, base_url=base_url)

        parameters = validated_data.get("parameters")
        if parameters is not None and len(parameters) != 0:
            for parameter in parameters:
                parameter_serializer = ParameterSerializer(data=parameter)
                if not parameter_serializer.is_valid():
                    return None

                parameter_serializer.save(endpoint=endpoint)

                if parameter_serializer is None:
                    return None

        return endpoint

    def update(self, instance, validated_data):
        parameters = []
        if validated_data.get("parameters") is not None:
            parameters = validated_data.pop("parameters")

        endpoint = super().update(instance=instance, validated_data=validated_data)

        if len(parameters) != 0:
            touched_parameters = []
            for parameter in parameters:
                parameter_id = parameter.get("id")
                if parameter_id is None:
                    parameter_serializer = ParameterSerializer(data=parameter)

                    if not parameter_serializer.is_valid():
                        return None

                    parameter_serializer.save(endpoint=endpoint)

                    if parameter_serializer is None or parameter_serializer.data is None:
                        return None

                    touched_parameters.append(parameter_serializer.data.get("id"))

                else:
                    parameter_instance = None
                    try:
                        parameter_instance = Parameter.objects.get(pk=parameter_id)
                    except Parameter.DoesNotExist:
                        return None

                    parameter_serializer = ParameterSerializer(instance=parameter_instance, data=parameter, partial=True)

                    if not parameter_serializer.is_valid():
                        return None

                    parameter_serializer.save()

                    if parameter_serializer is None or parameter_serializer.data is None:
                        return None

                    touched_parameters.append(parameter_id)

            # Remove parameters
            current_parameters = [parameter for parameter in instance.parameters.all()]
            for current_parameter in current_parameters:
                if current_parameter.id not in touched_parameters:
                    current_parameter.delete()

        return endpoint


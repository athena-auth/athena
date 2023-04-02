from rest_framework import serializers

from api.models import Provider
from api.security import hash_client_secret


class ProviderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(required=True, allow_blank=False)
    description = serializers.CharField(required=False, allow_blank=True)

    code_endpoint = serializers.CharField(required=True, allow_blank=False)
    token_endpoint = serializers.CharField(required=True, allow_blank=False)
    resource_endpoint = serializers.CharField(required=True, allow_blank=False)

    client_id = serializers.CharField(required=True, allow_blank=False)
    client_secret = serializers.CharField(required=True, allow_blank=False)
    public_key = serializers.CharField(required=True, allow_blank=False)
    scopes = serializers.ListField(child=serializers.CharField(required=True, allow_blank=False), required=True)
    redirect_uris = serializers.ListField(child=serializers.CharField(required=True, allow_blank=False), required=True)

    disabled = serializers.BooleanField(allow_null=False)

    def create(self, validated_data):
        validated_data["client_secret"] = hash_client_secret(validated_data["client_secret"])

        return Provider.objects.create(**validated_data)



from rest_framework.fields import ListField, IntegerField, CharField
from rest_framework.serializers import ModelSerializer
from api.models.scope import Scope


class ScopeSerializer(ModelSerializer):
    id = IntegerField(required=False)
    values = ListField(required=False)
    delimiter = CharField(required=False)

    class Meta:
        model = Scope
        fields = ["id", "delimiter", "values"]


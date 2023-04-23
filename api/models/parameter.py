from django.db.models import (Model,
                              CharField,
                              UniqueConstraint,
                              CASCADE,
                              ForeignKey,
                              Index)
from api.models import Endpoint


class Parameter(Model):
    name = CharField(null=False, max_length=255)
    value = CharField(null=False, max_length=255)
    endpoint = ForeignKey(Endpoint, on_delete=CASCADE, related_name="parameters")

    class Meta:
        db_table = "parameter"
        constraints = [UniqueConstraint(fields=["name", "value"], name="parameter_name_value_unique_index")]
        indexes = [Index(fields=["endpoint"])]

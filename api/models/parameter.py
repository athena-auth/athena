from django.db.models import (Model,
                              CharField,
                              UniqueConstraint,
                              CASCADE,
                              ForeignKey,
                              Index)
from api.models import Endpoint


class Parameter(Model):
    endpoint = ForeignKey(Endpoint, null=False, on_delete=CASCADE, related_name="parameters")

    name = CharField(null=False, blank=False, max_length=255)
    value = CharField(null=False, blank=False, max_length=255)

    class Meta:
        db_table = "parameter"
        constraints = [UniqueConstraint(fields=["endpoint", "name"], name="parameter_endpoint_name_unique_index")]
        indexes = [Index(fields=["name"]), Index(fields=["endpoint"])]

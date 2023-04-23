from django.db.models import (Model,
                              TextChoices,
                              CharField,
                              UniqueConstraint,
                              ForeignKey,
                              CASCADE, Index)
from api.models import Provider


class Endpoint(Model):

    class EndpointType(TextChoices):
        CODE = "code"
        TOKEN = "token"
        RESOURCE = "resource"

    class EndpointHttpMethod(TextChoices):
        GET = "GET"
        POST = "POST"
        DELETE = "DELETE"

    provider = ForeignKey(Provider, on_delete=CASCADE, related_name="endpoints")
    type = CharField(null=False, blank=False, choices=EndpointType.choices, max_length=255)
    http_method = CharField(null=False, blank=False, choices=EndpointHttpMethod.choices, max_length=255)
    base_url = CharField(null=False, blank=False, max_length=255)

    class Meta:
        db_table = "endpoint"
        constraints = [UniqueConstraint(fields=["type"], name="endpoint_type_unique_index")]
        indexes = [Index(fields=["provider"])]

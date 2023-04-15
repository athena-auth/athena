from django.db.models import (Model,
                              CharField,
                              BooleanField,
                              UniqueConstraint,
                              Index)
from django.contrib.postgres.fields import ArrayField
from api.utils.security import hash_client_secret


class Provider(Model):
    name = CharField(null=False, max_length=255)
    description = CharField(null=True, max_length=255)

    code_endpoint = CharField(null=False, max_length=255)
    token_endpoint = CharField(null=False, max_length=255)
    resource_endpoint = CharField(null=False, max_length=255)

    client_id = CharField(null=False, max_length=255)
    client_secret = CharField(null=False, max_length=255)
    public_key = CharField(null=False, max_length=255)
    scopes = ArrayField(base_field=CharField(max_length=255), null=False)
    redirect_uris = ArrayField(base_field=CharField(max_length=255), null=False)

    disabled = BooleanField(default=False, null=False)

    class Meta:
        db_table = "provider"
        constraints = [UniqueConstraint(fields=["name"], name="provider_name_unique_index"),
                       UniqueConstraint(fields=["client_id"], name="provider_client_id_unique_index")]
        indexes = [Index(fields=["name"]), Index(fields=["client_id"]), Index(fields=["disabled"])]

    def save(self, *args, **kwargs):
        self.client_secret = hash_client_secret(self.client_secret)
        super().save(*args, **kwargs)

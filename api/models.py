from django.db import models
from django.contrib.postgres.fields import ArrayField

from api.security import hash_client_secret


class Provider(models.Model):
    name = models.CharField(null=False, max_length=255)
    description = models.CharField(null=True, max_length=255)

    code_endpoint = models.CharField(null=False, max_length=255)
    token_endpoint = models.CharField(null=False, max_length=255)
    resource_endpoint = models.CharField(null=False, max_length=255)

    client_id = models.CharField(null=False, max_length=255)
    client_secret = models.CharField(null=False, max_length=255)
    public_key = models.CharField(null=False, max_length=255)
    scopes = ArrayField(base_field=models.CharField(max_length=255), null=False)
    redirect_uris = ArrayField(base_field=models.CharField(max_length=255), null=False)

    disabled = models.BooleanField(default=False, null=False)

    class Meta:
        db_table = "provider"
        constraints = [models.UniqueConstraint(fields=["client_id"], name="provider_client_id_unique_index")]
        indexes = [models.Index(fields=["name"]), models.Index(fields=["client_id"]), models.Index(fields=["disabled"])]

    def save(self, *args, **kwargs):
        self.client_secret = hash_client_secret(self.client_secret)
        super().save(*args, **kwargs)



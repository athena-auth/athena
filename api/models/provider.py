from django.db.models import (Model,
                              CharField,
                              BooleanField,
                              UniqueConstraint,
                              Index)


class Provider(Model):
    name = CharField(null=False, max_length=255)
    disabled = BooleanField(default=False, null=False)

    client_id = CharField(null=False, blank=False, max_length=255)
    client_secret = CharField(null=False, blank=False, max_length=255)
    scope = CharField(null=False, blank=False, max_length=255)
    redirect_uri = CharField(null=False, blank=False, max_length=255)

    public_key = CharField(null=True, blank=False, max_length=255)

    class Meta:
        db_table = "provider"
        constraints = [UniqueConstraint(fields=["name"], name="provider_name_unique_index"), UniqueConstraint(fields=["client_id"], name="provider_client_id_unique_index")]
        indexes = [Index(fields=["name"]), Index(fields=["disabled"]), Index(fields=["client_id"])]

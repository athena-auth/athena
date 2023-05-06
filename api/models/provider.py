from django.db.models import (Model,
                              CharField,
                              BooleanField,
                              Index)


class Provider(Model):
    name = CharField(null=False, blank=False, max_length=255, unique=True)
    disabled = BooleanField(null=False, default=False)
    client_id = CharField(null=False, blank=False, max_length=255, unique=True)
    client_secret = CharField(null=False, blank=False, max_length=255)

    redirect_uri = CharField(null=True, blank=False, max_length=255)
    public_key = CharField(null=True, blank=False, max_length=255)

    class Meta:
        db_table = "provider"
        indexes = [Index(fields=["name"]), Index(fields=["disabled"]), Index(fields=["client_id"])]

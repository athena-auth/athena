from django.db.models import (Model,
                              CharField,
                              BooleanField,
                              UniqueConstraint,
                              Index)


class Provider(Model):
    name = CharField(null=False, max_length=255)
    description = CharField(null=True, max_length=255)
    disabled = BooleanField(default=False, null=False)

    class Meta:
        db_table = "provider"
        constraints = [UniqueConstraint(fields=["name"], name="provider_name_unique_index")]
        indexes = [Index(fields=["name"]), Index(fields=["disabled"])]

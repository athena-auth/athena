from django.db.models import (Model,
                              CharField,
                              TextChoices,
                              CASCADE,
                              Index, OneToOneField)
from django.contrib.postgres.fields import ArrayField
from api.models import Provider


class Scope(Model):

    class ScopeDelimiter(TextChoices):
        SPACE = "space",
        COMMA = "comma",
        PERIOD = "period"

    provider = OneToOneField(Provider, null=False, on_delete=CASCADE, related_name="scope")

    delimiter = CharField(null=False,
                          blank=False,
                          choices=ScopeDelimiter.choices,
                          max_length=255,
                          default=ScopeDelimiter.SPACE)
    values = ArrayField(base_field=CharField(null=False, blank=False, max_length=255, unique=True),
                        null=False,
                        blank=False)

    class Meta:
        db_table = "scope"
        indexes = [Index(fields=["provider"])]

    def get_delimiter(self):
        if self.delimiter == self.ScopeDelimiter.SPACE:
            return " "
        elif self.delimiter == self.ScopeDelimiter.PERIOD:
            return "."
        elif self.delimiter == self.ScopeDelimiter.COMMA:
            return ","



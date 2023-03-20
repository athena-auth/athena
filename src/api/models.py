from django.db.models import Model, CharField


class User(Model):
    identifier = CharField(max_length=40, unique=True)
    USERNAME_FIELD = "identifier"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return False

# Django modules
from django.db.models import Model, CharField

class AutoPark(Model):
    AUTOPARK_NAME_MAX_LENGTH = 30

    name = CharField(
        max_length=AUTOPARK_NAME_MAX_LENGTH,
        unique=True,
    )

    def __str__(self):
        return f"Autopark with name:{self.name}"

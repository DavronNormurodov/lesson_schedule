from django.db.models import CharField, ManyToManyField

from shared.django.models import BaseModel


class Role(BaseModel):
    ROLE_CHOICES = (
        ("admin", "admin"),
        ("student", "student"),
        ("teacher", "teacher"),
    )

    title = CharField(max_length=100)
    unique_name = CharField(max_length=10, choices=ROLE_CHOICES)

    class Meta:
        ordering = ('-modified_date', )

    def __str__(self):
        return f"{self.title}"

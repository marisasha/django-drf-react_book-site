from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class LoginTryLogs(models.Model):
    user = models.ForeignKey(
        to = User, 
        on_delete=models.CASCADE, 
        db_index=True, 
        null=True
        )
    ip_address = models.CharField(
        max_length=40, 
        db_index=True
        )
    date = models.DateTimeField(
        default=timezone.now, 
        db_index=True
        )

    def __str__(self):
        return f'{self.ip_address} {self.date} {self.user}'

class Book(models.Model):
    title = models.CharField(
        verbose_name="Book title",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Book description",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    book_file = models.FileField(
        verbose_name="Book file",
        validators=[FileExtensionValidator(["pdf", "docx", "FB2"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="books",
    )
    # is_view

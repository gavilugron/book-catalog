from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    isbn           = models.CharField(
                        max_length=13,
                        blank=True,
                        null=True,
                        help_text="ISBN-13 of the book"
                    )
    published_date = models.DateField(
                        blank=True,
                        null=True,
                        help_text="Date when the book was published"
                    )
    created_at = models.DateTimeField(auto_now_add=True)
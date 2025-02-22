from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    available = models.BooleanField()

    class Meta:
        ordering = ["author"]
        verbose_name = "Book"
        verbose_name_plural = "Books"
        unique_together = [("title", "author")]
        indexes = [models.Index(fields=["title", "isbn"])]
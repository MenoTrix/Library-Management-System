from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    book_status = [("available", "available"), ("rented", "rented"), ("sold", "sold")]
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    author_image = models.ImageField(upload_to="images", blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    book_pages = models.IntegerField(null=True, blank=True)
    book_rental_by_dy = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    book_rental_period = models.IntegerField(null=True, blank=True)
    book_computed_rental = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=book_status, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name

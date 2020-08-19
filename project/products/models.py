from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)

    COLOR_CHOICES = (("red", "red"), ("blue", "blue"))
    color = models.CharField(
        max_length=16, null=False, blank=False, choices=COLOR_CHOICES
    )

    def __str__(self):
        return self.title

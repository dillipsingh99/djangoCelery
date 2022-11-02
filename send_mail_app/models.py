from django.db import models

class TryDemo(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    number = models.CharField(max_length=13)
    Country = models.CharField(max_length=20)

    def __str__(self):
        return self.name

from django.db import models

class Region(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.region

from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField()
    photo = models.ImageField(upload_to='images/about/', null=True, blank=True)
    description2 = models.TextField()

    def __str__(self):
        return self.title

from django.db import models

class Fallen(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
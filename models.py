from django.db import models

class OTU(models.Model):
    taxon_name = models.CharField(max_length=255)
    frequency = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taxon_name
django.contrib.auth.models.AbstractUser

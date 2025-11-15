from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    technology_stack = models.CharField(max_length=300, blank=True)
    documentation_url = models.URLField(blank=True)
    repository_url = models.URLField(blank=True)
    published_date = models.DateField(blank=True)

    def __str__(self):
        return self.name
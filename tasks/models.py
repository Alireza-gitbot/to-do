from django.db import models

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
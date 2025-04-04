'''App class models'''
from django.db import models

# Create your models here.

class Item(models.Model):
    '''Item Class for todo list'''
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return str(self.name)

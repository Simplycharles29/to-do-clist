from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering= ['-updated','-created']
        
    def __str__(self) -> str:
        return self.name



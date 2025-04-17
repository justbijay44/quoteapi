from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text[:10]} - {self.author}'
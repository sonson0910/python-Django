from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank = False, null = False)
    content = models.TextField(max_length = 1000, blank = False, null = False)
    create_time = models.DateField(default = timezone.now())

    def __str__(self):
        return self.title
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    consumer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    your_task = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    importance = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.your_task

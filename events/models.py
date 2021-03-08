from django.db import models
from django.conf import settings

from django.urls import reverse

# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    event_description = models.TextField(max_length=2000)
    event_date = models.DateField()
    event_url = models.URLField(help_text="Enter a url users can visit to learn more.")
    approved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='events', null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug':self.slug})

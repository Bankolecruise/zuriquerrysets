from django.db import models
from django.contrib.auth import get_user_model
from . import utils
from .managers import ActiveLinkManager



class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    objects =models.Manager()
    public = ActiveLinkManager()

    
    def __str__(self):
        return f"{self.identifier}"

    def save(self, *args, **kwargs):
        if not self.identifier:
            random_id = utils.generate_random_id()

            while Link.objects.filter(identifier=random_id).exists():
                random_id = utils.generate_random_id()

                self.identifier = random_id

        super().save(*args, **kwargs)

from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import capfirst
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.urls import reverse

class Post(models.Model):
    content = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(120)])
    name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.name}: {self.content}'

    def get_absolute_url(self):
        return reverse('joke', args=[str(self.id)])


    def save(self, *args, **kwargs):
        self.name = capfirst(self.name)
        if 'profanity' in self.content.lower():
            raise ValidationError("The content contains profanity.")
        super().save(*args, **kwargs)
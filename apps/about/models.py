from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class About(BaseModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    image = models.ImageField(upload_to='about_images/', default='img/default.jpg', blank=True, null=True)
    description_1 = RichTextField(null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    description_3 = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return f"{self.name}"
    
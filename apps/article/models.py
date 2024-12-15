from django.db import models

import uuid

from apps.common.models import BaseModel
from apps.user.models import CustomUser
from apps.category.models import Category, Tag

from ckeditor.fields import RichTextField

from django.utils.text import slugify
from django.urls import reverse


class Article(BaseModel):
    name = models.CharField(max_length=300, unique=True, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, db_index=True)
    image_1 = models.ImageField(upload_to='article_images/', default='img/default.jpg', null=True, blank=True)
    image_2 = models.ImageField(upload_to='article_images/', default='img/default.jpg', null=True, blank=True)
    image_3 = models.ImageField(upload_to='article_images/', default='img/default.jpg', null=True, blank=True)
    description_1 = RichTextField(null=True, blank=True)
    description_2 = RichTextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    author = models.ForeignKey(to='user.CustomUser', on_delete=models.CASCADE, related_name='articles_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles_category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles_tags')
    views = models.IntegerField(default=0)
    for_banner = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('article-detail', kwargs={'slug': self.slug})
    

class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments_article')
    user = models.ForeignKey(to=CustomUser, on_delete=models.SET_NULL, null=True, related_name='comments_user')
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, db_index=True, unique=True, null=True, blank=True)
    web_site = models.URLField(max_length=100, db_index=True, unique=True, null=True, blank=True)
    comment = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.name}"

from django.db import models
from django.urls import reverse

import os

def post_image_path(instance, filename):
    _, ext = os.path.splitext(filename)
    slug = instance.slug or "post"
    return f"post/{slug}/{slug}{ext}"

class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to=post_image_path, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post_detail', kwargs={'slug': self.slug})
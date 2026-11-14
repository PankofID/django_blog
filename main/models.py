import os

import nh3
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


POST_CONTENT_TAGS = {
    "a", "b", "blockquote", "br", "code", "del", "em", "h2", "h3", "h4",
    "h5", "h6", "hr", "i", "img", "ins", "li", "ol", "p", "pre", "s",
    "strong", "sub", "sup", "u", "ul",
}
POST_CONTENT_ATTRIBUTES = {
    "a": {"href", "title"},
    "img": {"src", "alt", "title"},
}


def sanitize_post_content(content):
    return nh3.clean(
        content,
        tags=POST_CONTENT_TAGS,
        attributes=POST_CONTENT_ATTRIBUTES,
        url_schemes={"http", "https", "mailto"},
    )


def post_image_path(instance, filename):
    _, ext = os.path.splitext(filename)
    slug = instance.slug or "post"
    return f"post/{slug}/{slug}{ext}"


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:post_list_by_category', kwargs={'slug': self.slug})

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
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

    @property
    def sanitized_content(self):
        return mark_safe(sanitize_post_content(self.content))

    def save(self, *args, **kwargs):
        self.content = sanitize_post_content(self.content)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('main:post_detail', kwargs={'slug': self.slug})

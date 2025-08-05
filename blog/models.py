from django.db import models
from django.utils.html import format_html
from datetime import datetime
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    image = models.ImageField(upload_to="category/")
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

    def image_tag(self):
        return format_html(
            '<div style="max-width:70px; white-space:nowrap;">'
            '<img src="/media/{}" style="width:70px; height:70px; border-radius:50%; " />'
            '</div>'.format(self.image)
        )

    image_tag.short_description = 'Image'


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = HTMLField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    image = models.ImageField(upload_to="post/")
    add_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html(
            '<div style="max-width:70px; white-space:nowrap;">'
            '<img src="/media/{}" style="width:70px; height:70px; border-radius:50%;  " />'
            '</div>'.format(self.image)
        )

    image_tag.short_description = 'Image'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

from django.contrib.admin import register, ModelAdmin
from .models import Category, Post, Contact


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('image_tag', 'title',  'add_date')
    list_filter = ['add_date']
    readonly_fields = ["add_date"]


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('image_tag', 'title',  'add_date')
    list_filter = ['category', 'add_date']
    readonly_fields = ["add_date"]


@register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')

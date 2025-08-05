
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('tinymce/', include('tinymce.urls')),
    path("", include("blog.urls"), name="blog")
]

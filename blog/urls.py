from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name='index'),
    path("blog/", views.blog, name="blog"),
    path("blogpost/<int:pk>", views.post_detail, name='post_detail'),
    path('categories/', views.all_categories, name='categories'),
    path('categories/<int:pk>/', views.category_posts, name='category_posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

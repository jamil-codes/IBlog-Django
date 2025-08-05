from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Contact, Post, Category
from django.core.paginator import Paginator

POSTS_PER_PAGE = 6


def index(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # Validation
        if not name or not email or not message:
            context["error"] = "All fields are required. Please fill out the form completely."
        else:
            try:
                validate_email(email)
            except ValidationError:
                context["error"] = "Please enter a valid email address."
            else:
                Contact.objects.create(name=name, email=email, message=message)
                context["info"] = "Thanks for reaching out—stories connect us, and yours matters."

    # Get latest 3 posts
    latest_posts = Post.objects.select_related(
        "category").order_by("-add_date", "-pk")[:3]

    context["latest_posts"] = latest_posts

    return render(request, "blog/index/index.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def blog(request):
    posts = Post.objects.all().order_by("-add_date", "-pk")
    paginator = Paginator(posts, POSTS_PER_PAGE)  # Show 6 posts per page
    page_number = request.GET.get("page", 1)
    posts_obj = paginator.get_page(page_number)

    return render(request, "blog/blog.html", {"posts": posts_obj})


def all_categories(request):
    categories = Category.objects.all().order_by("title")
    return render(request, "blog/categories.html", {"categories": categories})


def category_posts(request, pk):
    category = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(
        category=category).order_by("-add_date", "-pk")

    paginator = Paginator(post_list, POSTS_PER_PAGE)  # Show 6 posts per page
    page_number = request.GET.get("page", 1)
    posts = paginator.get_page(page_number)

    return render(request, "blog/category_posts.html", {
        "category": category,
        "posts": posts,
    })

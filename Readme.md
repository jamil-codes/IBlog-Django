
# 📝 IBlog - A Minimal, Elegant Django Blog Template

**IBlog** is a modern, extensible blog template built with Django 5.2. It provides a clean foundation for developers or content creators to quickly launch a blog with categories, a contact form, TinyMCE integration, and full admin support.

---

## 🚀 Features

- ✅ Django 5.2 Compatible
- 🖋️ Rich-text post editor using TinyMCE
- 🗂️ Category-based blog filtering
- 📬 Contact form with validation
- 🖼️ Image uploads for posts and categories
- 🔎 Paginated blog list views
- 🛠️ Admin interface enhanced with Jazzmin
- 📱 Responsive layout with custom styling
- 📦 Pre-seeded `db.sqlite3` for testing

---

## 📁 Project Structure

```
IBlog_Django/
│
├── db.sqlite3                # Pre-populated DB (posts, categories, contact)
├── manage.py
├── requirements.txt
├── IBlog_Presentation.pdf    # Project overview (slides)
│
├── blog/
│   ├── models.py             # Category, Post, Contact
│   ├── views.py              # Views: blog, detail, categories, contact
│   ├── urls.py
│   ├── admin.py              # Admin config with image previews
│   ├── templates/
│   │   └── blog/
│   │       ├── layout.html
│   │       ├── navbar.html
│   │       ├── footer.html
│   │       ├── blog.html
│   │       ├── post_detail.html
│   │       ├── categories.html
│   │       ├── category_posts.html
│   │       └── index/
│   │           ├── index.html
│   │           ├── contact.html
│   │           ├── hero.html
│   │           └── latest_blogs.html
│   ├── migrations/
│   └── ...
│
├── core/                     # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── media/                    # Uploaded media
│   ├── category/
│   └── post/
│
└── static/                   # Static assets
    ├── style.css
    └── images/
```

---

## 💡 Models Overview

```python
class Category(models.Model):
    title, description, image, add_date

class Post(models.Model):
    title, content (TinyMCE), image, category (FK), add_date

class Contact(models.Model):
    name, email, message, created_at
```

---

## 📦 Requirements

```
asgiref==3.9.1
Django==5.2.4
django-jazzmin==3.0.1
django-tinymce==4.1.0
pillow==11.3.0
sqlparse==0.5.3
tzdata==2025.2
```

Install with:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Local Setup Instructions

1. **Clone the Repository**
###
2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run Migrations**

```bash
python manage.py migrate
```

4. **(Optional) Use the Seeded Database**

No setup needed — `db.sqlite3` is already populated with sample categories, posts, and contact entries.

5. **Run the Development Server**

```bash
python manage.py runserver
```

6. **Admin Panel Login**

Access: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

- Username: `admin`
- Password: `admin`

---

## ✨ Pages Overview

- `/` – Homepage (latest blogs, hero section)
- `/blogs/` – All blog posts with pagination
- `/categories/` – All blog categories
- `/category/<id>/` – Posts filtered by category
- `/post/<id>/` – Individual post detail
- `/contact/` – Contact form

---

## 🧩 Customization Tips

- **Styling**: Edit `static/style.css` to match your design taste.
- **Rich Text**: Posts use `TinyMCE`, allowing headings, lists, quotes, and images.
- **Admin UI**: Managed with [Jazzmin](https://github.com/farridav/django-jazzmin) for a modern look.
- **Pagination**: Included on blogs and category views (6 per page).

---

## 📬 Contact Form

Contact messages are saved in the database via the `Contact` model and can be viewed through the admin panel.

---

## 📌 License

This project is licensed under the **MIT License**. Feel free to use, modify, and share.

---

> Built for learning, writing, and clarity. Ready to fork and expand.

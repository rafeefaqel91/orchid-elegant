# 🌸 Orchid Elegant - Girls Clothing E-commerce Platform

![Django](https://img.shields.io/badge/Django-4.2-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![License](https://img.shields.io/badge/License-MIT-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📋 Project Overview

**Orchid Elegant** is a fully functional e-commerce web application built with Django, designed specifically for selling girls' clothing. The platform provides a seamless shopping experience with product browsing, shopping cart management, order processing, and user authentication.

### 🎯 Project Goals
- Create a responsive e-commerce website for girls' clothing
- Implement secure user authentication and authorization
- Provide AJAX-powered shopping cart functionality
- Integrate email notifications for orders and registration
- Deliver a clean, user-friendly interface

---

## 🚀 Live Demo

🔗 **Live Website:** [https://yourusername.pythonanywhere.com](https://yourusername.pythonanywhere.com)  
📁 **GitHub Repository:** [https://github.com/yourusername/orchid-elegant](https://github.com/yourusername/orchid-elegant)

---

## ✨ Features

### 👤 User Features
| Feature | Status |
|---------|--------|
| User registration with validation | ✅ |
| Secure login/logout | ✅ |
| Browse products by category | ✅ |
| Search products | ✅ |
| View product details with image gallery | ✅ |
| Add to cart (AJAX - no page reload) | ✅ |
| Update cart quantities dynamically | ✅ |
| Remove items from cart | ✅ |
| Checkout with shipping information | ✅ |
| View order history | ✅ |
| Contact form with email notifications | ✅ |

### 👑 Admin Features
| Feature | Status |
|---------|--------|
| Product management (CRUD) | ✅ |
| Category management | ✅ |
| Order management and status updates | ✅ |
| View and respond to customer messages | ✅ |

### 🔧 Technical Features
| Feature | Status |
|---------|--------|
| AJAX for cart operations | ✅ |
| Email integration (welcome, order confirmations) | ✅ |
| Responsive design (Bootstrap 5) | ✅ |
| Form validation and CSRF protection | ✅ |
| SQLite database (MySQL ready) | ✅ |
| Password hashing for security | ✅ |

---

## 📱 Responsive Design

The website is fully responsive and optimized for:
- 💻 **Desktop** (1200px+)
- 📱 **Tablet** (768px - 1199px)
- 📱 **Mobile** (320px - 767px)

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Backend** | Django 4.2, Python 3.8+ |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Database** | SQLite (development), MySQL ready |
| **AJAX** | jQuery for async operations |
| **Email** | SMTP integration (Gmail) |
| **Version Control** | Git & GitHub |
| **Deployment** | PythonAnywhere / Render ready |

---

## 📁 Project Structure
orchid-elegant/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── CODE_FREEZE.md
├── orchid_elegant/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── store/
│ ├── init.py
│ ├── admin.py
│ ├── models.py # Database models
│ ├── views.py # Application logic
│ ├── forms.py # Form validation
│ ├── urls.py # URL routing
│ ├── context_processors.py
│ ├── templatetags/
│ ├── templates/ # HTML templates
│ │ └── store/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── product_list.html
│ │ ├── product_detail.html
│ │ ├── cart.html
│ │ ├── checkout.html
│ │ ├── order_history.html
│ │ ├── about.html
│ │ ├── contact.html
│ │ ├── login.html
│ │ └── register.html
│ └── static/ # CSS, JS files
│ └── store/
│ ├── css/
│ ├── js/
│ └── images/
├── media/ # User uploaded files
└── staticfiles/ # Collected static files


---

## 🚀 Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

**1. Clone the repository**
```bash
git clone https://github.com/rafeefaqel91/orchid-elegant.git
cd orchid-elegant


djangoPy3env\Scripts\activate

pip install -r requirements.txt

# Copy example environment file
cp .env.example .env

# Generate secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Copy the output and paste it in .env file

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput

python manage.py runserver




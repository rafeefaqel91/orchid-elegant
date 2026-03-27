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

Access the application

Website: http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

🔒 Security Features
Security Feature	Implementation
CSRF Protection	✅ Active on all forms
Password Hashing	✅ Django's pbkdf2_sha256
SQL Injection Prevention	✅ Django ORM with parameterized queries
XSS Protection	✅ Auto-escaping enabled
Session Security	✅ Secure session management
Form Validation	✅ All forms validated
🌐 API Integrations
Email Integration
Welcome Emails: Sent to new users upon registration

Order Confirmations: Sent after successful checkout

Contact Form: Sends messages to admin email

Google Maps Integration
Location Map: Embedded in contact page (API key required)

🎯 AJAX Implementation
The following features use AJAX for better user experience:

Feature	Description
Add to Cart	Adds items without page reload
Update Cart	Updates quantities dynamically
Remove Item	Removes items instantly
Cart Total	Real-time total calculation
Example AJAX Code:
$.ajax({
    url: '/add-to-cart/',
    type: 'POST',
    headers: {'X-CSRFToken': getCookie('csrftoken')},
    data: JSON.stringify({product_id: productId}),
    success: function(response) {
        updateCartCount(response.cart_count);
        showNotification('Item added to cart!');
    }
});

📊 Database Schema
Model	Fields	Purpose
Category	name, slug, description, image	Product categories
Product	name, slug, category, price, description, image, stock	Product details
Cart	user, session_key, created_at	Shopping cart
CartItem	cart, product, quantity	Items in cart
Order	user, order_number, address, total_amount, status	Customer orders
OrderItem	order, product, quantity, price	Items in orders
ContactMessage	name, email, subject, message	Customer inquiries
🧪 Testing
Run tests with:

python manage.py test

Test Coverage
✅ User registration and authentication

✅ Product listing and details

✅ Cart operations (AJAX)

✅ Checkout process

✅ Form validation

✅ Email notifications

📈 Development Sprint
Sprint	Days	Activities
Sprint 1	Days 1-2	Analysis, Design, Database Setup
Sprint 2	Days 3-5	Core Features (Auth, Products)
Sprint 3	Days 6-8	Advanced Features (Cart, AJAX, Email)
Sprint 4	Days 9-10	Testing, Bug Fixes, Deployment
🚀 Deployment
Deployed on PythonAnywhere
Live URL: https://yourusername.pythonanywhere.com

Deployment Steps
Set DEBUG = False in settings.py

Configure ALLOWED_HOSTS with your domain

Set environment variables on platform

Collect static files: python manage.py collectstatic --noinput

Run migrations: python manage.py migrate

Configure WSGI file

Reload web app

🎓 What I Learned
Django Framework: Deep understanding of MVC architecture, models, views, and templates

AJAX Integration: Creating seamless user experiences without page reloads

Responsive Design: Making websites work on all devices with Bootstrap

Security Best Practices: CSRF protection, password hashing, SQL injection prevention

Database Design: Creating efficient relationships between models

Deployment: Taking a project from local to production on PythonAnywhere

Agile Methodology: Working in sprints with daily standups and sprint reviews

🔮 Future Enhancements
Online payment integration (Stripe/PayPal)

Product reviews and ratings

Wishlist feature

Advanced search filters

Social media login (Google, Facebook)

Product recommendations based on browsing

Discount/Coupon system

Email newsletters for promotions

🐛 Known Issues
No known issues. All features are working as expected. The project has been thoroughly tested on all devices and browsers.

🤝 Contributing
This is a solo project for educational purposes as part of the Full stack developing bootcamp with Axsos academy. Suggestions and feedback are welcome!

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👩‍💻 Author
Rafeef Aqel
GitHub: @rafeefaqel91

Email: rafeef.aqel@gmail.com

🙏 Acknowledgments
Django Documentation

Bootstrap 5

Font Awesome

All tutorials and resources used during the 10-day project

📊 Project Status
Item	Status
Code Freeze	✅ Completed on March 27, 2026
Deployment	✅ Ready / Live
Documentation	✅ Complete
Testing	✅ Passed
GitHub Repository	✅ Public
Trello Board	✅ Complete
Ready for Submission	✅ Yes
⭐ If you found this project helpful, please star it on GitHub!

© 2026 Orchid Elegant. All rights reserved.


# E-Point: University Project Documentation

## 1. Project Overview

E-Point is a contemporary e-commerce web application developed using the Django framework. The system is intended to provide a comprehensive online shopping experience encompassing secure user authentication, product discovery, shopping cart management, checkout processing, seller administration, messaging, and AI-driven product recommendations.

The application adheres to Django's Model-View-Template (MVT) architectural pattern. It is designed for local deployment and can be extended for production with minimal modification.

## 2. Objectives

The principal objectives of this project are as follows:

- Develop a fully functional e-commerce platform that supports both buyers and sellers.
- Implement secure user registration, login, and password reset mechanisms.
- Provide intuitive product browsing, detailed product views, and category-based filtering.
- Implement a persistent shopping cart and a robust checkout process.
- Support seller administration through a dedicated dashboard.
- Incorporate an internal messaging system for buyer-admin and buyer-seller communication.
- Deploy a recommendation engine to suggest related products.
- Generate printable invoices in PDF format.

## 3. Technology Stack

The project has been constructed utilizing the following technologies:

- Backend: Python 3.14 and Django 5.2.8.
- Frontend: HTML5, CSS3, JavaScript, and Bootstrap 5.
- Database: SQLite for development.
- Machine learning: pandas and scikit-learn.
- Payment integration: Stripe using environment-based credentials.
- PDF generation: ReportLab.
- Version control: Git.

## 4. System Architecture

### 4.1 Django Applications

The solution is segmented into multiple Django applications, each responsible for a specific domain:

- accounts: Manages user registration, login, email OTP verification, password reset, and seller/admin dashboard functionality.
- shop: Manages the product catalogue, product detail pages, seller product creation, offer banners, and informational pages.
- orders: Implements shopping cart behavior, checkout flow, order storage, Stripe payment integration, and invoice generation.
- messaging: Facilitates internal messaging for communication between buyers, sellers, and administrators.

### 4.2 Core Workflow

- A visitor arrives on the home page and browses available products.
- Registered users may add products to their cart and proceed to checkout.
- Checkout creates an order record and initiates a Stripe checkout session.
- Order status is updated following successful payment or cancellation.
- Sellers and administrators may review orders, modify statuses, and administer promotional content.

## 5. Key Features

### 5.1 User Accounts

- Email-based registration with OTP verification.
- Secure login and logout functionality.
- Password reset through OTP verification.
- Access to a seller dashboard restricted to superusers.

### 5.2 Product Catalog

- The shop application manages product categories and product information.
- Product detail pages display related product recommendations.
- Administrators can list new products and maintain inventory levels.
- An offer banner model enables dynamic marketing promotion content.

### 5.3 Shopping Cart and Orders

The shopping cart is implemented with a session-backed cart class that synchronizes with a database representation when the user is authenticated. This ensures cart persistence across sessions and devices for logged-in users.

- Users can add and remove products and view cart totals.
- Checkout generates Order and OrderItem records.
- Stripe checkout session integration manages payment processing.
- Order outcomes are tracked through success and cancellation callbacks.
- Users may review their order history at any time.

### 5.4 Messaging System

- Users may send messages to the site administrator.
- Users may communicate directly with product sellers from the product page.
- Received messages are displayed in a centralized inbox.
- Receivers may reply to individual messages.

### 5.5 AI Recommendation Engine

This project includes a machine learning-based recommendation engine that employs TF-IDF vectorization and cosine similarity to identify products related to the current item. When the recommendation engine cannot identify similar products, the system falls back to a category-based recommendation strategy.

### 5.6 PDF Invoice Generation

The application produces printable invoice documents using ReportLab. Each invoice includes order metadata, purchased items, quantities, prices, and the total amount.

## 6. Data Model Summary

### 6.1 Accounts Application

The accounts application contains the EmailOTP model, which stores one-time passwords issued for registration and password reset procedures.

### 6.2 Shop Application

- Category: Represents product categories with name and slug fields.
- Product: Stores category, seller, title, description, price, image, stock quantity, and creation timestamp.
- OfferBanner: Stores marketing banner content and active status.

### 6.3 Orders Application

- Order: Contains user reference, total amount, creation date, and status.
- OrderItem: Represents products associated with an order, with quantity and price details.
- CartModel: A one-to-one cart record for each authenticated user.
- CartItemModel: Individual cart item records linked to the user cart.

### 6.4 Messaging Application

The messaging application stores communication records between users, including sender, receiver, associated product, content, and timestamp.

## 7. Installation and Setup

### 7.1 Prerequisites

- Python 3.10 or later.
- Git.
- A command-line interface.

### 7.2 Setup Steps

Follow the steps below to prepare the application environment and execute the project:

- Clone the repository and navigate to the project directory.
- Create and activate a Python virtual environment.
- Install project dependencies from requirements.txt.
- Apply Django database migrations.
- Create a superuser account for administrative access.
- Optionally configure Stripe environment variables for checkout functionality.
- Launch the Django development server.
- Open the application in a web browser at http://127.0.0.1:8000/.

## 8. Application Usage

### 8.1 Buyer Workflow

- Browse the home page and product listing pages.
- Select a product to view detailed information.
- Add desired products to the shopping cart.
- Proceed to checkout and complete payment through Stripe test mode.
- Review completed orders from the order history page.

### 8.2 Seller and Administrator Workflow

- Log in using a superuser account.
- Access the Sell page to add new products to the catalogue.
- Use the dashboard to monitor order volume, revenue, and product performance.
- Update order statuses and manage promotional banners.

### 8.3 Messaging Workflow

- Contact the administrator through the contact form.
- Send messages to sellers from the product detail page.
- View received messages in the inbox.
- Reply to messages directed to the authenticated user.

## 9. URLs and Routes

The principal application routes are listed below:

- / → Home page.
- /products/ → Product listing page.
- /product/<id>/ → Product detail page.
- /sell/ → Product creation page for superusers.
- /product/<id>/add-to-cart/ → Add an item to the shopping cart.
- /accounts/register/ → User registration page.
- /accounts/login/ → User login page.
- /accounts/logout/ → Logout endpoint.
- /accounts/dashboard/ → Seller dashboard.
- /orders/cart/ → Shopping cart view page.
- /orders/checkout/ → Checkout page.
- /orders/list/ → Order history page.
- /orders/invoice/<id>/ → Download invoice document.
- /messages/inbox/ → Messaging inbox.
- /messages/contact-admin/ → Contact administrator page.
- /messages/product/<id>/send/ → Send a message to the seller.
- /messages/reply/<id>/ → Reply to a received message.

## 10. Deployment Considerations

- The development server is executed with python manage.py runserver.
- For production deployment, a WSGI or ASGI server such as Gunicorn is recommended.
- SQLite is appropriate for development but should be replaced with PostgreSQL or MySQL for production deployments.
- Stripe API keys must be managed securely using environment variables.
- Media files are served from the media directory, while static assets are served from the static directory.

## 11. Future Enhancements

- Deploy the application to a cloud platform such as AWS or Heroku.
- Integrate additional payment gateways such as Razorpay and PayPal.
- Add user wishlists and product review functionality.
- Implement real-time notifications using WebSockets.
- Migrate from SQLite to PostgreSQL for improved scalability.
- Expose RESTful APIs using Django REST Framework for mobile applications.

## 12. Conclusion

E-Point represents a complete e-commerce system that combines secure user authentication, comprehensive product management, robust cart and order processing, internal messaging, and AI-driven recommendations. The project demonstrates modular design principles through Django applications and leverages contemporary libraries to deliver a practical and extensible platform.

## 13. References

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/
- Python Documentation: https://docs.python.org/3/
- Stripe API Documentation: https://stripe.com/docs
- Pandas Documentation: https://pandas.pydata.org/docs/
- Scikit-learn Documentation: https://scikit-learn.org/stable/


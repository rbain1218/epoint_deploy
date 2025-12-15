# E-Point | Modern E-Commerce Platform

E-Point is a fully functional, modern e-commerce web application built with Django. It features a responsive UI inspired by major platforms like Amazon and Flipkart, offering a seamless shopping experience with user authentication, product browsing, cart management, and order processing.

## 🚀 Features

### 🛍️ Shopping Experience
- **Modern UI**: Clean, responsive design with a Hero banner, category navigation, and card-based product grid.
- **Product Search**: Integrated search bar in the navbar for quick product discovery.
- **Product Details**: Detailed product pages with image galleries, specifications, and "Buy Now" / "Add to Cart" options.
- **Category Browsing**: Filter products by categories (Mobiles, Fashion, Electronics, etc.).

### 👤 User Accounts
- **Authentication**: Secure Login, Registration, and Logout functionality.
- **User Dashboard**: View order history and manage profile settings.
- **Seller Dashboard**: Superusers can list new products, manage stock, and view sales.

### 🛒 Order Management
- **Shopping Cart**: Add/remove items, update quantities, and view total cost.
- **Checkout**: Streamlined checkout process.
- **Order History**: Track past orders and status.

### 💬 Messaging System
- **Contact Admin**: Users can send messages to the admin/support directly from the dashboard.
- **Seller Chat**: Potential buyers can message sellers directly from the product page.
- **Inbox**: Centralized inbox for viewing and replying to messages.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3 (Custom + Bootstrap 5), JavaScript
- **Database**: SQLite (Default)
- **Styling**: Custom CSS with modern design variables (Inter font, vibrant palette).

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### Prerequisites
- Python 3.8 or higher
- Git

### Steps

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/rbain1218/epoint_deploy.git
    cd epoint_deploy
    ```

2.  **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**
    ```bash
    python3 manage.py migrate
    ```

5.  **Create a Superuser (Admin)**
    ```bash
    python3 manage.py createsuperuser
    ```

6.  **Run the Server**
    ```bash
    python3 manage.py runserver
    ```

7.  **Access the App**
    - Open your browser and go to: `http://127.0.0.1:8000/`

## 📂 Project Structure

```
epoint_deploy/
├── accounts/       # User authentication and profile management
├── epoint/         # Project settings and main URLs
├── media/          # User-uploaded content (Product images)
├── messaging/      # Internal messaging system
├── orders/         # Cart and Order logic
├── shop/           # Product catalog and home page
├── static/         # CSS, JS, and static images
├── templates/      # Global templates (base.html)
└── manage.py       # Django management script
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request for any feature additions or bug fixes.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

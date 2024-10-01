# Product Management System

This project is a simple Django application that provides an API and frontend interface for managing products. The system includes product creation, validation, and listing via a RESTful API and a user-friendly frontend built with Tailwind CSS and Django templates.

## Features

- **Product API**: 
  - Create products via POST requests.
  - Retrieve all products via GET requests.
  - Validates product data, ensuring a positive price and non-empty product name.
  
- **Frontend**: 
  - A simple HTML page for adding products.
  - Displays the list of products in a responsive table.
  - AJAX-based submission of product data using Fetch API.
  - Automatically updates product list on successful submission.

## Technologies

- **Backend**: Django, Django REST Framework (DRF) for API
- **Frontend**: HTML, JavaScript (Fetch API), Tailwind CSS
- **Database**: SQLite (default Django database)
- **API Validation**: DRF Serializers for validation
- **Templating**: Django Templates with Tailwind CSS

## Getting Started

### Prerequisites

- Python 3.7+
- Django 3.x or 4.x
- Django REST Framework (DRF)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/product-management-system.git
   cd product-management-system
   ```

2. **Create a virtual environment** and activate it:

   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/macOS
   # OR
   env\Scripts\activate      # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations** to set up the database:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Open the app** in your browser:

   ```
   http://127.0.0.1:8000/products/
   ```

### API Endpoints

- **Create a Product** (POST): `/products/`
  - Example request body (JSON):
    ```json
    {
      "name": "Product Name",
      "description": "Product Description",
      "price": 19.99
    }
    ```

- **Get All Products** (GET): `/products/`
  - Returns a list of products in JSON format.

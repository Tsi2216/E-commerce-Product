# Django Administration Interface

## Overview

This project is a Django-based web application that provides an administration interface for managing various entities such as groups, categories, and products. The interface allows for easy management and authorization of users, as well as the ability to manage product data efficiently.

## Features

- User Authentication and Authorization
- Manage User Groups
- Create, Read, Update, and Delete (CRUD) operations for Products and Categories
- Responsive design for optimal use across devices

## Installation

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.x
- Django
- pip (Python package installer)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Tsi2216/E-commerce-Product.git
   cd e-commerce-api

    Create a virtual environment:
    bash

python -m venv venv

Activate the virtual environment:

    On Windows:
    bash

venv\Scripts\activate

On macOS/Linux:
bash

    source venv/bin/activate

Install the required packages:
bash

pip install -r requirements.txt

Run migrations to set up the database:
bash

python manage.py migrate

Create a superuser to access the admin interface:
bash

python manage.py createsuperuser

Start the development server:
bash

    python manage.py runserver

    Access the admin interface:
    Open your web browser and go to http://127.0.0.1:8000/admin to access the Django admin panel.

Usage

    Log in with the superuser credentials you created.
    You can manage:
        Groups: Create and manage user groups for authorization.
        Products: Add, edit, or delete product information.
        Categories: Organize products into categories.

Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

    Django Documentation
    Open Source Community

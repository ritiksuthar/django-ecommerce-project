OnStore E-Commerce Website
An interactive e-commerce web application built with Django and Bootstrap. This project features essential e-commerce functionalities, including product listings, product details, cart management, Razorpay payment integration, and user authentication.

Features
User Authentication: Register, log in, and manage user profiles.
Product Listings: Display products with images, descriptions, and prices.
Shopping Cart: Add, update, and remove products from the cart.
Product Details Page: View detailed product descriptions.
Responsive Design: Fully responsive UI using Bootstrap.
Payment Integration: Online payment processing with Razorpay.
Admin Dashboard: Manage products, users, and orders from the Django admin panel.

Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite (can be replaced with PostgreSQL/MySQL)
Payment Gateway: Razorpay
Version Control: Git & GitHub

Installation Instructions
1. Clone the Repository
git clone https://github.com/yourusername/ecommerce_project.git
cd ecommerce_project
2. Create and Activate a Virtual Environment

# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
env\Scripts\activate

# On Mac/Linux
source env/bin/activate

3. Install Dependencies
Install the required Python packages using requirements.txt:
pip install -r requirements.txt

5. Set Up the Database
Apply migrations to create the necessary database tables:
python manage.py migrate

7. Create a Superuser
Create a Django admin superuser to manage the site:
python manage.py createsuperuser

9. Run the Development Server
Start the Django development server:
python manage.py runserver
Open the server in your browser at http://127.0.0.1:8000/.

Usage Instructions
Visit http://127.0.0.1:8000/ to explore the e-commerce platform.
Sign up or log in to start adding products to your cart.
Proceed to checkout and complete payments using the Razorpay gateway.

Project Structure
/ecommerce_project
    ├── /cart                # Cart-related views, templates, and URLs
    ├── /products            # Product-related views, templates, and URLs
    ├── /ecommerce_project   # Main project settings and configurations
    ├── manage.py            # Django project management script
    └── requirements.txt     # Project dependencies

Future Enhancements
Wishlist Feature: Allow users to save products for later.
Product Reviews & Ratings: Enable user feedback and ratings for products.
Order History: Display past orders for logged-in users.
Multiple Payment Gateways: Integrate more payment options like PayPal.

License
This project is open-source and available under the MIT License.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1.Fork the repository.
2.Create a feature branch (git checkout -b feature/YourFeature).
3.Commit your changes (git commit -m 'Add YourFeature').
4.Push to the branch (git push origin feature/YourFeature).
5.Create a Pull Request.

Contact
For any questions or feedback, feel free to reach out:
Author: Ritik Suthar
Email: theritiksuthar@gmail.com
GitHub: github.com/ritiksuthar


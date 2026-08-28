# CodeShop — Simple E-commerce Store (Django + SQLite)

Built for the Code Alpha "Simple E-commerce Store" task.

## Features
- **Product listings** with images, price, and stock status
- **Product details page**
- **Shopping cart** (session-based — add, update quantity, remove)
- **Order processing** — checkout form, order creation, stock deduction, order confirmation
- **User registration / login / logout** (Django auth)
- **Order history** per user
- **Admin panel** to manage products and view/manage orders
- **SQLite** database (via Django ORM) storing products, users, and orders

## Project structure
```
manage.py
ecommerce_project/     # Django project settings & root urls
store/                 # Main app: models, views, forms, cart logic, urls, admin
templates/store/       # HTML templates
static/store/css/      # Stylesheet
seed.py                # Seeds 5 sample products + a superuser
```

## Setup

1. Create a virtual environment (recommended) and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run migrations (database is already included with sample data, but if you
   want to start fresh, delete `db.sqlite3` first):
   ```bash
   python manage.py migrate
   ```

3. (Optional — already done in the included db) Seed sample products and an admin user:
   ```bash
   python manage.py shell < seed.py
   # or: python seed.py
   ```
   This creates 5 sample products and a superuser: **admin / admin12345**

4. Run the dev server:
   ```bash
   python manage.py runserver
   ```

5. Visit:
   - `http://127.0.0.1:8000/` — the shop
   - `http://127.0.0.1:8000/admin/` — admin panel (login: admin / admin12345)

## How it works

- **Cart**: stored in the Django session as `{product_id: quantity}` (see `store/cart.py`).
  No login needed to add items to the cart, but you must be logged in to check out.
- **Checkout**: `/checkout/` takes shipping details, creates an `Order` + `OrderItem`s
  from the cart, reduces product stock, clears the cart, and redirects to a confirmation page.
- **Models** (`store/models.py`):
  - `Product` — name, description, price, stock, image_url
  - `Order` — user, status, total, shipping details
  - `OrderItem` — order, product, price, quantity

## Ideas to extend (good for going beyond the base task)
- Add product categories/search & filtering
- Add product reviews/ratings
- Hook up real payments (Stripe/Razorpay) instead of the `pending` status flow
- Add email confirmation on order placement
- Move cart from session to a DB-backed `Cart` model tied to the user (persists across devices)
- Add pagination to the product list
- Write Django `TestCase` unit tests (there's a manual smoke-test flow you can adapt)

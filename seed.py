import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()
from store.models import Product
from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')

products = [
    ("Wireless Mouse", "Ergonomic wireless mouse with USB receiver.", 19.99, 50, "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400"),
    ("Mechanical Keyboard", "RGB backlit mechanical keyboard, blue switches.", 59.99, 30, "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400"),
    ("USB-C Hub", "7-in-1 USB-C hub with HDMI and card reader.", 34.50, 25, "https://images.unsplash.com/photo-1591290619762-ef0d2e5f0e97?w=400"),
    ("Laptop Stand", "Adjustable aluminum laptop stand.", 27.00, 40, "https://images.unsplash.com/photo-1611267254323-4db7b39c732c?w=400"),
    ("Webcam 1080p", "Full HD webcam with built-in microphone.", 42.99, 0, "https://images.unsplash.com/photo-1587826080692-f439465f7ac0?w=400"),
]
for name, desc, price, stock, img in products:
    Product.objects.get_or_create(name=name, defaults=dict(description=desc, price=price, stock=stock, image_url=img))

print("Seeded", Product.objects.count(), "products, superuser admin/admin12345")

import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker

import random

from products.models import Brand, Product, ProductImages, Review

from django.contrib.auth.models import User


def seed_brand(n):
    fake =  Faker()

    images = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg',
              '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']

    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f"brand/{images[random.randint(0,9)]}"
        )



def seed_products(n):
    fake = Faker()

    flag_types = ['NEW', 'SALE', 'FEATURE']

    brands = Brand.objects.all()

    images = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg',
              '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']

    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            # flag = flag_types[random.randint(0,2)],
            flag = flag_types[2],
            price = round(random.uniform(1.99, 99.99),2),
            image = f"brand/{images[random.randint(0,9)]}",
            sku = random.randint(10000, 99999),
            subtitle = fake.text(max_nb_chars=450),
            description = fake.text(max_nb_chars=10000),
            brand = brands[random.randint(0, len(brands))],
        )



def seed_reviews(n):
    fake = Faker()

    users = User.objects.all()

    products = Product.objects.all()

    for _ in range(n):
        Review.objects.create(
            user = users[random.randint(0, len(users)-1)],
            product = products[random.randint(0, len(products)-1)],
            review = fake.text(max_nb_chars=500),
            rate = random.randint(1, 5),
            created_at = fake.date_time_this_year(),
        )



def seed_users(n):
    fake = Faker()

    for _ in range(n):
        User.objects.create(
            username= fake.name().replace(" ", ""),
            password = "MoH.1822"
        )




seed_products(100)
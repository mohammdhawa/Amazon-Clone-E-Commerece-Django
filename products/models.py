from django.db import models

from taggit.managers import TaggableManager

from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
FLAG_TYPES = (
        ("SALE", "SALE"),
        ("NEW", "NEW")
    )

# RATE_CHOICES = [
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#     ]


class Product(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=20, choices=FLAG_TYPES)
    image = models.ImageField(max_length=)
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=500)
    description = models.TimeField(50000)
    brand = models.ForeignKey('Brand', related_name="product_brand", 
                              on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()




class ProductImages(models.Model):
    product = models.ForeignKey(Product, 'product_image', related_name='product_images',
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')



class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')

    def __str__(self):
        return self.name



class Review(models.Model):
    user = models.ForeignKey(User, related_name='review_user', 
                             on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, related_name='product_review', 
                                on_delete=models.CASCADE)
    review = models.TextField(max_length=10000)
    rate = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(default=timezone.now)




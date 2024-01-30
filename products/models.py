from django.db import models

from taggit.managers import TaggableManager

from django.contrib.auth.models import User

from django.utils import timezone

from django.utils.text import slugify

from django.utils.translation import gettext_lazy as _

# Create your models here.
FLAG_TYPES = (
    ("SALE", "SALE"),
    ("NEW", "NEW"), 
    ('FEATURE', "FEATURE")
)


class Product(models.Model):
    name = models.CharField(_('name'), max_length=120)
    flag = models.CharField(_('flag'), max_length=20, choices=FLAG_TYPES)
    price = models.FloatField(_('price'))
    image = models.ImageField(_('image'), upload_to='product')
    sku = models.IntegerField(_('sku'), )
    subtitle = models.TextField(_('subtitle'), max_length=500)
    description = models.TextField(_('description'), max_length=50000)
    brand = models.ForeignKey('Brand', verbose_name=_('brand'), related_name="product_brand", 
                              on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    @property # now this is as a column in db
    def review_count(self):
        reivews = self.product_review.all().count()
        return reivews
    
    @property # now this is as a column in db
    def avg_rate(self):
        reviews = self.product_review.all()
        
        if reviews:
            return round(sum(rev.rate for rev in reviews) / len(reviews), 1)
        return 0
    
    class Meta:
        # class within a model that contains metadata about the model itself. 
        # anything I write here .. will be applied on every query that return from this object
        ordering = ['id'] # to get the last item first and so on
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



class ProductImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('product'), related_name='product_images',
                                on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='productimages')

    def __str__(self):
        return str(self.product)



class Brand(models.Model):
    name = models.CharField(_('name'), max_length=100)
    image = models.ImageField(_('image'), upload_to='brand')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='review_user', 
                             on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='product_review', 
                                on_delete=models.CASCADE)
    review = models.TextField(_('review'), max_length=10000)
    rate = models.IntegerField(_('rate'), choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{str(self.product)} - {str(self.user)}"




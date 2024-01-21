from django.contrib import admin

from .models import Product, ProductImages, Review, Brand

# Register your models here.
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 3 # number of empty forms to display



class ProductReviews(admin.TabularInline):
    model = Review
    extra = 2



class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline, ProductReviews]


admin.site.register(Product, ProductAdmin)

admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
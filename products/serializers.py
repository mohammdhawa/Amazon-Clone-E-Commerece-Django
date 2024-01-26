from rest_framework import serializers

from .models import Brand, Product, Review


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"
    

    def get_review_count(self, object):
        reivews = object.product_review.all().count()
        return reivews



class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"
    

    def get_review_count(self, object):
        reivews = object.product_review.all().count()
        return reivews



class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"



class BrandDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"
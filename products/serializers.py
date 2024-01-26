from rest_framework import serializers

from .models import Brand, Product, Review


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"
    

    def get_review_count(self, object):
        reivews = object.product_review.all().count()
        return reivews
    
    def get_avg_rate(self, obj):
        reviews = obj.product_review.all()
        
        if reviews:
            return round(sum(rev.rate for rev in reviews) / len(reviews), 1)
        return 0




class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"
    

    def get_review_count(self, object):
        reivews = object.product_review.all().count()
        return reivews
    
    def get_avg_rate(self, obj):
        reviews = obj.product_review.all()
        
        if reviews:
            return round(sum(rev.rate for rev in reviews) / len(reviews), 1)
        return 0



class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"



class BrandDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"
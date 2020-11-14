from django.contrib.auth.models import User
from .models import Customer, Product, Category, Choice, Cart
from rest_framework import serializers

#ModelSerializer 사용
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('addr', 'membership')

class UserSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()#1대1관계인 customerserializer 추가

    class Meta:
        model = User
        fields = ('id', 'username', 'customer')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'category', 'price', 'color', 'size')

#customizing nested 
class ProductListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'id : {} price : {}'.format(value.id, value.price)


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"



class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = "__all__"#모든 필드 serialize

class CategorySerializer(serializers.ModelSerializer):
    products = ProductListingField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'products')












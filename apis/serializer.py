from pyexpat import model
from unicodedata import category, name
from attr import field, fields
from rest_framework import serializers
from .models import  author, bookings, celebrity ,book
class celebrity_serializers(serializers.ModelSerializer):
    class Meta:
        model = celebrity
        fields = ('id' ,'celebrity_name','celebrity_price','celebrity_tag','description','celebrity_image')
        field = "__all__"     
class booking(serializers.ModelSerializer):
    class Meta:
        model = bookings
        fields =('id','Name','Occasion','Video_date','To')
        field = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only = True , many = True)
    class Meta:
        model = author
        field = '__all__'
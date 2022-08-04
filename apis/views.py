
from itsdangerous import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from yaml import serialize
from .models import  author, bookings, celebrity
from .serializer import AuthorSerializer, BookSerializer, booking, celebrity_serializers
# from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import  generics

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def celebrity_data(request):
    if request.method == 'GET':
        celebritydata = celebrity.objects.all()
        Serializer = celebrity_serializers(celebritydata,many = True)
        return Response(Serializer.data)
    elif request.method == 'POST':
        Serializer = celebrity_serializers(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
        return Response({'Message':'successfully created'})


@api_view(['GET','POST','DELETE'])
def celebrity_single_data(request,id):
    if request.method == 'GET':
        celebritydata1 = celebrity.objects.get(id=id)
        Serializer = celebrity_serializers(celebritydata1,many=False)
        return Response(Serializer.data)
    elif request.method == 'POST':
        celebrityid = celebrity.objects.get(id=id)
        Serializer = celebrity_serializers(instance=celebrityid,data =request.data)
        if Serializer.is_valid():
            Serializer.save()
        return Response({'Message':'successfully update celebrity = ' +id})
    elif request.method == 'DELETE':
        celebrityid = celebrity.objects.get(id=id)
        celebrityid.delete()
        return Response({'message':'Delete account successfully'})

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def celebrity_bookings(request):
    if request.method == 'GET':
        bookingdata = bookings.objects.all()
        Serializer = booking(bookingdata,many = True)
        return Response(Serializer.data)
    elif request.method == 'POST':
        Serializer = booking(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
        return Response({'Message':'successfully created'})


 
    
# class AuthorlistView(generics.ListCreateAPIView):
#     queryset = author.objects.all()
#     Serializer_class = AuthorSerializer

# class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = author.objects.all()
#     Serializer_class = AuthorSerializer

# class BooklistView(generics.ListCreateAPIView):
#     queryset = author.objects.all()
#     Serializer_class = BookSerializer

# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = author.objects.all()
#     Serializer_class = BookSerializer    
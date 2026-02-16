from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CartItemView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = AuthorSerializer

    

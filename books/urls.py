from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('authors/', AuthorListView.as_view()),
    path('books/', BookListView.as_view()),
    path('cart-items/', CartItemView.as_view()),
]

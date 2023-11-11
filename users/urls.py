# users/urls.py
from django.urls import path, include
from users import views
from .views import UserDetail

urlpatterns = [
  path('', include('djoser.urls')),
  path('', include('djoser.urls.authtoken')),
  path('users/<int:id>/', UserDetail.as_view()),
]
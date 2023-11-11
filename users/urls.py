# users/urls.py
from django.urls import path, include
from users import views
from users.views import UserDetail

urlpatterns = [
  path('', include('djoser.urls')),
  path('', include('djoser.urls.authtoken')),
  path('delete_user/', UserDetail.as_view()),
]
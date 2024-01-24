
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register),
    path('login/', views.MyTokenObtainPairSerializer.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
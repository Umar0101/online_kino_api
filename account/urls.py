from django.urls import path, include 
from rest_framework_simplejwt.views import TokenObtainPairView


from .views import RegisterUserView, ActivateView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('activate/', ActivateView.as_view()),
    path('login/',TokenObtainPairView.as_view())
]
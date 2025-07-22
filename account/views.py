from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect

from .serializers import RegisterSerializer
from .models import CustomUser

class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегистрировались", status=201)

class ActivateView(APIView):
    def get(self, request):
        activation_code = request.query_params.get('u')
        user = get_object_or_404(CustomUser, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ""
        user.save()
        return redirect('https://google.com')

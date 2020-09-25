from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.http import HttpResponse
# import json

from django.contrib.auth import authenticate, logout, login

from .forms import RegisterUser

from .serializers import UsersSerializer
from .models import Profile


@csrf_exempt
def registerPage(request):
    form = RegisterUser()

    if request.method == 'POST':
        form = RegisterUser(request.POST)

    if form.is_valid():
        form.save()
        return redirect('login')

    context = {'form': form}

    return render(request, 'register.html', context)


@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'success.html')

    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

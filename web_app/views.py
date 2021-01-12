from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import resolve, reverse
from django.core.exceptions import ObjectDoesNotExist
from . import models
# Create your views here.
def has_permission(user, url, method):
    role = models.Role.objects.get(user=user)
    permissions = models.RoleHasPermisson.objects.filter(role=role)
    permissions = [i.permission.permission_id for i in permissions]
    try:
        check_permission = models.Permission.objects.get(method=method, url=url).permission_id
    except ObjectDoesNotExist:
        check_permission = None
    if check_permission in permissions:
        return True
    else:
        return False
    

class LoginView(View):
    def check_local_ip(self):
        pass


    def get(self, request):
        return render(request, 'web_app/login.html')


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'web_app/login.html')

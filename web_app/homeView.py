from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import resolve, reverse
from .views import has_permission

class Index(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        url_name = resolve(request.path).url_name
        url_name = reverse(url_name)
        if has_permission(request.user, url_name, request.method):
            return HttpResponse("Hello")
        else:
            return HttpResponse("No permission")
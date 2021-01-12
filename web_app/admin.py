from django.contrib import admin
from . import models
# Register your models here.

class showUser(admin.ModelAdmin):
    list_display = ['username', 'password']

class showRole(admin.ModelAdmin):
    list_display = ['user', 'role_name']

class showPermission(admin.ModelAdmin):
    list_display = ['permission_name', 'method', 'url']

class showRoleHasPermisson(admin.ModelAdmin):
    list_display = ["role", 'permission']


admin.site.register(models.User, showUser)
admin.site.register(models.Role, showRole)
admin.site.register(models.Permission, showPermission)
admin.site.register(models.RoleHasPermisson, showRoleHasPermisson)
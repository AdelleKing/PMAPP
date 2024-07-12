from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)    
    created_on = models.DateField(auto_now_add=True)

class Domain(DomainMixin):
    pass

class CustomUser(AbstractUser):
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='customuser_set')  # Add related_name
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')
    
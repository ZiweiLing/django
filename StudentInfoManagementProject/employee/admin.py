from django.contrib import admin
from . import models
from .models import Employee, CID

# Register your models here.
admin.site.register(models.Employee)
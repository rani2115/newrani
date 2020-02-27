from django.contrib import admin

# Register your models here.
from .models import MyTable

admin.site.register(MyTable)
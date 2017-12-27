from django.contrib import admin
from .models import Article,Suggest,Review

# Register your models here.

admin.site.register([Article,Suggest,Review])

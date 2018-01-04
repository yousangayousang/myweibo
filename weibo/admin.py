from django.contrib import admin
from .models import Article,Suggest,Review

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display=('id','title','created_time')

@admin.register(Suggest)
class SuggestAdmin(admin.ModelAdmin):
	list_display=('name','Suggest_email','suggest_time')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display=('user_name','user','review_time')

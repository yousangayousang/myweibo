# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import SuggestForm,ReviewForm,UserForm,Input_UserForm
from .models import Article,Suggest,Review
from django.shortcuts import get_object_or_404,get_list_or_404,reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
import markdown

# Create your views here.

def get_queryset(request):
	article=Article.objects.all()

	article_list=Paginator(article,5)

	article_number=request.GET.get("num")

	try:

		article_list1=article_list.page(article_number)

	except EmptyPage:
		article_list1=article_list.page(article_list.num_pages)

	except PageNotAnInteger:
		article_list1=article_list.page(1)
	return render(request,'weibo/index.html',{'article_list' : article_list1})

def boke(request,article_id):

	form=ReviewForm()
	suggest=Review.objects.filter(article_id=article_id)
	number=len(suggest)
	boke=get_object_or_404(Article,pk=article_id)
	boke.body=markdown.markdown(boke.body,
									extensions=[
										'markdown.extensions.extra',
										'markdown.extensions.codehilite',
										'markdown.extensions.toc',
									])
	boke.views=boke.views+1
	boke.save()
	suggest_list=Paginator(suggest,3)
	suggest_num=request.GET.get("num")

	try:
		suggestlist=suggest_list.page(suggest_num)
	except EmptyPage:
		suggestlist=suggest_list.page(suggest_list.num_pages)
	except PageNotAnInteger:
		suggestlist=suggest_list.page(1)
	return render(request,"weibo/blog.html",{'number':number,'suggest_list':suggestlist,'boke':boke,'form':form})


def denglu(request):
	if not request.user.is_authenticated():
		form=Input_UserForm()
		return render(request,"weibo/input.html",{"form" : form})
	else :
		user=request.user.get_full_name()
		username=request.user.get_username()
		return render(request,"weibo/input.html",{'user':user,'username':username})

def denglu1(request):
	if request.method == 'POST':
		form=Input_UserForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['input_username']
			password=form.cleaned_data['input_password']
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
				else:
					error='该账户已被禁用'
					return render(request,'weibo/error.html',{'error' : error})
			else:
				error='密码错误,请重新登录'
				return render(request,'weibo/error.html',{'error' : error})
			return HttpResponseRedirect("/denglu/")

def zhuce(request):
	form=UserForm(request.POST)
	return render(request,"weibo/support.html",{'form' : form})

def zhuce1(request):
	if request.method == 'POST':
		form=UserForm(request.POST)
		if form.is_valid():
			password=form.cleaned_data['password']
			egan_password=form.cleaned_data['egan_password']
			username=form.cleaned_data['username']
			user=form.cleaned_data['user']
			email=form.cleaned_data['email']
			if password != egan_password:
				error='密码输入不正确'
				return render(request,'weibo/error.html',{'error' : error})
			if len(password) <= 7:
				error='密码过短，请重新输入'
				return render(request,'weibo/error.html',{'error' : error})
			if len(user) <= 7 :
				error='账号过短，请重新输入'
				return render(request,'weibo/error.html',{'error' : error})
			if User.objects.filter(username=user) :
				error='账号已存在'
				return render(request,'weibo/error.html',{'error' : error})
			if User.objects.filter(email=email):
				error='邮箱已注册'
				return render(request,'weibo/error.html',{'error' : error})
			user=User.objects.create_user(user,email,password)
			user.last_name=username
			user.save()
			error='注册成功'
			return render(request,'weibo/error.html',{'error' : error})

		else:
			return HttpResponse('数据未接收到')
	else:
		return HttpResponse('访问失败')

def pinglun(request,article_id):
	if request.POST:
		if not request.user.is_authenticated():
			error='请先登录！'
			return render(request,'weibo/error.html',{'error' : error})
		else :
			forms=ReviewForm(request.POST)
			if forms.is_valid():
				review=forms.cleaned_data['review']
				form=Review()
				form.user_name=request.user.get_full_name()
				form.user=request.user.get_username()
				form.review=review
				form.article=get_object_or_404(Article,pk=article_id)
				form.save()
				return HttpResponseRedirect(reverse('weibo:boke',kwargs={'article_id' : article_id}))
	else:
		return HttpResponse('访问失败！')

def dengchu(request):
	logout(request)
	return HttpResponseRedirect('/denglu/')

def liuyan(request):
	form=SuggestForm()
	return render(request,'weibo/contact.html',{'form' : form})

def liuyan1(request):
	if request.method == 'POST':
		form=SuggestForm(request.POST)
		if form.is_valid():
			phone=form.cleaned_data['phone']
			name=form.cleaned_data['name']
			email=form.cleaned_data['Suggest_email']
			suggest=form.cleaned_data['suggest']
			if len(phone) != 11:
				error='请输入正确的电话号码'
				return render(request,'weibo/error.html',{'error' : error})
			forms=Suggest(name=name,phone=phone,suggest=suggest,Suggest_email=email)
			form.save()
			error='建议提交成功'
			return render(request,'weibo/error.html',{'error' : error})

		else:
			return HttpResponse('数据接受失败！')
	else:
		return HttpResponse('访问失败！')

def we(request):
	return render(request,'weibo/about.html')

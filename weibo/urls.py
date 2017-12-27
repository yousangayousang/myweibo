from django.conf.urls import url
from . import views

app_name='weibo'

urlpatterns=[ 
	url(r'^$',views.get_queryset,name='queryset'),
	url(r'^(?P<article_id>[0-9]+)/boke/$',views.boke,name='boke'),
	url(r'^denglu1/$',views.denglu1,name='denglu1'),
	url(r'^denglu/$',views.denglu,name='denglu'),
	url(r'^zhuce/$',views.zhuce,name='zhuce'),
	url(r'^zhuce1/$',views.zhuce1,name='zhuce1'),
	url(r'^(?P<article_id>[0-9]+)/pinglun/$',views.pinglun,name='pinglun'),
	url(r'^dengchu/$',views.dengchu,name='dengchu'),
	url(r'^liuyan/$',views.liuyan,name='liuyan'),
	url(r'^liuyan1/$',views.liuyan1,name='liuyan1'),
	url(r'^wei/$',views.we,name='we'),
]
from django.db import models

# Create your models here.

#文章字段
class Article(models.Model):
	 title = models.CharField('标题', max_length=200)
	 subtitle=models.CharField('副标题',max_length=200)
	 body=models.TextField('正文')
	 created_time=models.DateTimeField('创建时间',auto_now_add=True)
	 last_time=models.DateTimeField('修改时间',auto_now=True)

	 views=models.PositiveIntegerField('浏览量',default=0)
	 likes=models.PositiveIntegerField('点赞量',default=0)

#用户建议字段
class Suggest(models.Model):
	name=models.CharField('姓名',max_length=50)
	Suggest_email=models.EmailField('邮箱')
	phone=models.CharField('联系电话',max_length=11)
	suggest=models.TextField('建议')
	suggest_time=models.DateTimeField('建议时间',auto_now_add=True)

#用户评论字段
class Review(models.Model):
	user_name=models.CharField('姓名',max_length=200)
	user=models.CharField('账号',max_length=20)
	review=models.TextField('评论')
	article=models.ForeignKey('Article',verbose_name='评论文章',)
	review_time=models.DateTimeField('评论时间',auto_now_add=True)


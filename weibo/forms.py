from django import forms
from .models import Review,Suggest

class UserForm(forms.Form):
	egan_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '请重新输入密码：', 'class' : 'text' }))

	username=forms.CharField(widget=forms.TextInput(attrs={'placeholder' : '请输入昵称：', 'class' : 'text' }))

	user=forms.CharField(widget=forms.TextInput(attrs={'placeholder' : '请输入账号：', 'class' : 'text' }))


	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '请输入密码：', 'class' : 'text' }))


	email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : '请输入email：', 'class' : 'text' }))




class Input_UserForm(forms.Form):
	input_username=forms.CharField(widget=forms.TextInput(attrs={'placeholder' : '请输入账号：', 'class' : 'text' }))
	input_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '请输入密码：', 'class' : 'text' }))

class SuggestForm(forms.ModelForm):
	class Meta:
		model=Suggest
		fields=['name','phone','Suggest_email','suggest']
		widgets={
			'name': forms.TextInput(attrs={
				'placeholder' : '请输入姓名：',
				'class' : 'text',
				'height' : 40
				}),
			'phone' : forms.TextInput(attrs={
				'placeholder' : '请输入电话：',
				'class' : 'text',
				'height' : 40
				}),
			'Suggest_email' : forms.EmailInput(attrs={
				'placeholder' : '请输入邮箱：',
				'class' : 'text',
				'height' : 40
				}),
			'suggest' : forms.Textarea(attrs={
				'placeholder' : '您的意见是：',
				'class' : 'text'
				})
	}

class ReviewForm(forms.ModelForm):
	class Meta:
		model=Review
		fields=['review']
		widgets={
			'review' : forms.Textarea(attrs={
				'placeholder' : '想要说什么....'
				})
	}


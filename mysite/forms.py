#-*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from mysite import models

class ContactForm(forms.Form):
	CITY =[
		['TP', 'Taipei'],
		['TY', 'Taoyuang'],
		['TV', 'Taichung'],
		['TN', 'Tainan'],
		['KS', 'Kaoshiung'],
		['NA', 'Others'],
	]
	user_name = forms.CharField(label='您的姓名', max_length=50, initial='匿名')
	user_city = forms.ChoiceField(label='居住城市', choices=CITY)
	user_school = forms.BooleanField(label='是否為在學學生', required=False)
	user_email = forms.EmailField(label='電子郵件')
	user_message = forms.CharField(label='您的意見', widget=forms.Textarea)
	
class LoginForm(forms.Form):
	username = forms.CharField(label='姓名', max_length=10)
	password = forms.CharField(label='密碼', widget=forms.PasswordInput())
	
	
class OrderForm(forms.ModelForm):
	class Meta:
		models = models.Order
		fields = ['full_name', 'address', 'phone']
	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['full_name'].label = '收件人姓名'
		self.fields['address'].label = '郵件地址'
		self.fields['phone'].label = '連絡電話'
		

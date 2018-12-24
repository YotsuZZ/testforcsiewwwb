#-*- encoding: utf-8 -*-
from django import forms

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
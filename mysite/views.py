from django.shortcuts import render
from mysite import models, forms
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django import template
from django.http import HttpResponse
from django.template import RequestContext


def index(request, cat_id=0):
	all_products = None
	
	if cat_id > 0:
		try:
			category = models.Category.objects.get(id=cat_id)
		except:
			category = None
		
		if category is not None:
			all_products = models.Product.objects.filter(category=category)
			
	
	if all_products is None:
		all_products = models.Product.objects.all()
		
	
	paginator = Paginator(all_products, 4)
	p = request.GET.get('p')
	try:
		products = paginator.page(p)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
		
	return render(request, 'index.html', locals())
	
	if request.user.is_authenticated:
		username = request.user.username
	messages.get_messages(request)
	
	return render(request, 'index.html', locals())


def detail(request, id):
	try:
		product = models.Product.objects.get(id=id)
		images = models.Photo.objects.filter(product=product)
	except:
		pass
	return render(request, 'detail.html',locals())
	
def contact(request):
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			message = "感謝您的來信，我們會盡速處理。"
			user_name = form.cleaned_data['user_name']
			user_city = form.cleaned_data['user_city']
			user_school = form.cleaned_data['user_school']
			user_email = form.cleaned_data['user_email']
			user_message = form.cleaned_data['user_message']
			
			mail_body = u'''
學生姓名:{}
居住城市:{}
是否為在學:{}
反映意見:如下
{}'''.format(user_name, user_city, user_school, user_message)
			email = EmailMessage(  '來自資工系二手書交易平台',
									mail_body,
									user_email,
									['qweasd73468010@gmail.com'])
			email.send()
		else:
			message = "請檢察您輸入的資訊是否正確!"
	else:
		form = forms.ContactForm()
	return render(request, 'contact.html', locals())
	
def login(request):
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			login_name = request.POST['username'].strip()
			login_password = request.POST['password']
			user = authenticate(username=login_name, password=login_password)
			if user is not None:
					if user.is_active:
						auth.login(request, user)
						messages.add_message(request, messages.SUCCESS, '成功登入')
						return redirect('/')
					else:
						messages.add_message(request, messages.WARNING,  '密碼錯誤 請再從新檢查一次')
			else:
				messages.add_message(request, messages.WARNING, '找不到使用者')
		else:
			messages.add_message(request, messages.INFO,  '請檢察欄位內容')
	else:
		login_form = forms.LoginForm()
	return render(request, 'login.html', locals())
				
				
def logout(request):
	auth.logout(request)
	messages.add_message(request, messages.INFO, "成功登出")
	return redirect('/')

		
		
@login_required(login_url='/login/')		
def userinfo (request):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			user = User.object.get(username=username)
			userinfo = models.User.object.get(user=user)
		except:
			pass
	return render(request, 'userinfo.html', locals())
	html = template.render(locals())
	return HttpResponse(html)
	
	
	
def product(request, product_id):

	try:
		product = models.Product.objects.get(id=product_id)
	except:
		product = None
	

	return render(request, 'product.html', locals())
	html = template.render(locals())
	return HttpResponse(html)
			
			
			
			
			
			
			
			
			
			
			
			
			
			

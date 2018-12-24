from django.contrib import admin
from mysite import models
class ProductAdmin(admin.ModelAdmin):
	list_display = ('category1', 'sku', 'name', 'stock', 'price')
	ordering = ('category1',)

	
	
	
	
admin.site.register(models.Maker)
admin.site.register(models.Profile)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category1)
# Register your models here.


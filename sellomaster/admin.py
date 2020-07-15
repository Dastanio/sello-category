from django.contrib import admin

from .models import Product, Rubric
admin.site.register(Rubric)


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'price', 'number','date_publeshed', 'rubric',)
	list_display_links = ('title', 'description')
	search_fields = ('title', 'description', )
admin.site.register(Product, ProductAdmin)
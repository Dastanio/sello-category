from django.shortcuts import render
from .models import Product, Rubric

def index(request):
	products = Product.objects.all()
	rubrics = Rubric.objects.all()
	context = {
		'products':products,
		'rubrics': rubrics,
	}
	return render(request, 'index.html', context)

def by_rubric(request, rubric_id):
	bbs = Product.objects.filter(rubric=rubric_id)
	rubrics = Rubric.objects.all()
	current_rubric = Rubric.objects.get(pk=rubric_id)
	context = {
		'rubrics':rubrics,
		'bbs':bbs,
		'current_rubric':current_rubric,
	}
	return render(request, 'by_rubric.html', context)
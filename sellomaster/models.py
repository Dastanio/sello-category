from django.db import models
import datetime


class Rubric(models.Model):
	name = models.CharField(max_length=40, db_index=True)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Категории"
		verbose_name = 'Категорий'
		ordering = ['name']

class Product(models.Model):
	rubric = models.ForeignKey(Rubric, null = True, on_delete=models.PROTECT, verbose_name='Рубрика')
	title = models.CharField('Заголовок',max_length=30)
	description = models.TextField('Описания')
	number = models.CharField('Номер телефона',max_length=50)
	price = models.IntegerField('Цена',default=0)

	date_publeshed = models.DateTimeField(auto_now_add=True, db_index=True)
	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = "Товары"









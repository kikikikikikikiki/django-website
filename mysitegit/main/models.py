from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)
	image_card = models.CharField(max_length=400)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series


# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())

	tutorial_series= models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.tutorial_title


class CircleCategory(models.Model):
	circle_category = models.CharField(max_length=200)
	circle_summary = models.CharField(max_length=200)
	circle_slug = models.CharField(max_length=200)
	circle_card = models.CharField(max_length=400)

	class Meta:
		verbose_name_plural = "Circle Categories"

	def __str__(self):
		return self.circle_category

class CircleSeries(models.Model):
	circle_series = models.CharField(max_length=200)
	circle_category = models.ForeignKey(CircleCategory, default=1, related_name="series1", verbose_name="Circle Category 1", on_delete=models.SET_DEFAULT)
	circle_category2 = models.ForeignKey(CircleCategory, default=1, related_name="series2", verbose_name="Circle Category 2", on_delete=models.SET_DEFAULT)
	circle_category3 = models.ForeignKey(CircleCategory, default=1, related_name="series3", verbose_name="Circle Category 3", on_delete=models.SET_DEFAULT)
	circle_category4 = models.ForeignKey(CircleCategory, default=1, related_name="series4", verbose_name="Circle Category 4", on_delete=models.SET_DEFAULT)
	circle_summary = models.CharField(max_length=200)
	circle_image = models.CharField(max_length=400)
	circle_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Circle Series"

	def __str__(self):
		return self.circle_series


# Create your models here.
class Circle(models.Model):
	circle_title = models.CharField(max_length=200)
	#circle_content = models.TextField()
	circle_published = models.DateTimeField("date published", default=datetime.now())

	circle_series= models.ForeignKey(CircleSeries, default=1, verbose_name="Circle Series", on_delete=models.SET_DEFAULT)
	circle_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.circle_title


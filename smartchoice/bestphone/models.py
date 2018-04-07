from django.db import models

# Create your models here.

class table_11(models.Model):
	model_no = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length = 50)
	price = models.FloatField()
	users_review = models.FloatField()
	expert_review = models.FloatField()
	features = models.FloatField()
	price1 = models.FloatField()
	newer = models.FloatField()
	result = models.FloatField()
	LINK = models.CharField(max_length = 1000,null = True)

	def __str__(self):
		return self.name

class table_12(models.Model):
	model_no = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length = 50)
	price = models.FloatField()
	users_review = models.FloatField()
	expert_review = models.FloatField()
	features = models.FloatField()
	price1 = models.FloatField()
	newer = models.FloatField()
	result = models.FloatField()

	def __str__(self):
		return self.name

class table_13(models.Model):
	model_no = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length = 50)
	price = models.FloatField()
	users_review = models.FloatField()
	expert_review = models.FloatField()
	features = models.FloatField()
	price1 = models.FloatField()
	newer = models.FloatField()
	result = models.FloatField()

	def __str__(self):
		return self.name	

class table_14(models.Model):
	model_no = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length = 50)
	price = models.FloatField()
	users_review = models.FloatField()
	expert_review = models.FloatField()
	features = models.FloatField()
	price1 = models.FloatField()
	newer = models.FloatField()
	result = models.FloatField()

	def __str__(self):
		return self.name					
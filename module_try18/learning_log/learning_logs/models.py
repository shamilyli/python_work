from django.db import models

# Create your models here.

class Topic(models.Model):

	""" for user study topic"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		"""return the models charaters"""
		return self.text

class Entry(models.Model):
	"""knowledge learn from relevant topic"""
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""return the models of charaters"""
		return self.text[:50]+ "..."
		
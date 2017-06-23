from django.db import models

# Create your models here.
class Topic(models.Model):
	"""user study theme """
	text = models.CharField(max_length =200)

	def __str__(self):
		return self.text


class Entry(models.Model):
	"""learned some knowledge from the theme """
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added= models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural='entries'

	def __str__(self):
		"""return the model of text """ 
		return self.text[:50] + "..."
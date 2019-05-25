from django.db import models
from django.conf import settings
from django.urls import reverse
import misaka

from datetime import datetime    

class YTdata(models.Model):
	created_at = models.DateTimeField(default=datetime.now)
	search = models.CharField(max_length=100,default='null')
	title = models.CharField(max_length=100,default='null')

	def __unicode__(self):
		return self.title

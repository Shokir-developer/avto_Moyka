from django.db import models


class Mijoz(models.Model):
	nomer = models.CharField(max_length=100, null=True)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nomer
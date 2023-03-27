from django.db import models
from core.models import BaseModel
from ckeditor.fields import RichTextField


class Post(BaseModel):
	title = models.CharField(max_length=200, null=True, blank=True)
	body = RichTextField()

	def __str__(self):
		return self.title

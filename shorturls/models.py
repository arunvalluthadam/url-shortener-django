from django.db import models
from django.core.urlresolvers import reverse
from .basechanger import decimal2base_n, base_n2decimal
from .random_str import rand_str

# Create your models here.

class Link(models.Model):
	url = models.URLField()
	
	def get_absolute_url(self):
		return reverse("link_show", kwargs={"pk": self.pk})
	
	@staticmethod
	def shorten(link):
		l = Link.objects.get_or_create(url=link.url)
		return str(decimal2base_n(l.pk))+rand_str()
		
	@staticmethod
	def expand(slug):
		link_id = int(base_n2decimal(slug))
		l = Link.objects.get(pk=link_id)
		return l.url
		
	
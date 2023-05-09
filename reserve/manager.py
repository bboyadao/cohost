from django.db import models
from django.db.models import Q


class RoomManager(models.Manager):
	def get_queryset(self):
		return super(RoomManager, self).get_queryset()

	def available(self, date_in, date_out):
		"""
		list available room by datetime range handle gap and full range
		"""
		if date_out > date_in:
			return self.get_queryset().filter(

				Q(reserve=None) | Q(
					Q(reserve__checkout_at__lt=date_in) & Q(reserve__checkin_at__lt=date_out)
				)
			)
		raise ValueError("")

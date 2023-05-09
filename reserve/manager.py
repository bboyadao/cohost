from django.db import models
from django.db.models import Q


class RoomManager(models.Manager):
	def get_queryset(self):
		return super(RoomManager, self).get_queryset()

	def available(self, date_in, date_out):
		return self.get_queryset().exclude(
				Q(
					Q(reserve__checkin_at__lte=date_in) & Q(reserve__checkout_at__gte=date_in) |
					Q(reserve__checkin_at__lte=date_out) & Q(reserve__checkout_at__gte=date_out)
				)
		)

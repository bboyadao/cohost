from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils import timezone

from reserve.manager import RoomManager


class Room(models.Model):
	name = models.CharField(max_length=255)
	objects = RoomManager()

	def __str__(self):
		return f"{self.name}"

	def is_available_in(self, date_in, date_out, reserve) -> bool:
		"""
		:reserve: is prevented update record.
		Check overlap by qs.
		If not exists return True
		"""
		qs = self.reserve_set.filter(
			Q(
				Q(checkin_at__lte=date_in) & Q(checkout_at__gte=date_in) |
				Q(checkin_at__lte=date_out) & Q(checkout_at__gte=date_out)
			)
		).exclude(pk=reserve.pk)
		return not qs.exists()


class Reserve(models.Model):
	room = models.ForeignKey("reserve.Room", on_delete=models.PROTECT)
	guest = models.ForeignKey("auth.User", on_delete=models.PROTECT)
	checkin_at = models.DateTimeField()
	checkout_at = models.DateTimeField()

	def clean(self):
		if self.checkout_at < timezone.now() or self.checkin_at < timezone.now():
			raise ValidationError("Checkin and out day must be greater than current time")

		if self.checkout_at < self.checkin_at:
			raise ValidationError({
				"checkin_at": "Checkout day must be greater than checkin day.",
				"checkout_at": "Checkout day must be greater than checkin day."
			})

		if self.room.is_available_in(self.checkin_at, self.checkin_at, self) is False:
			raise ValidationError({
				"room": f"This room '{self.room.name}' Placed by someone please select another room"}
			)

	def __str__(self):
		return f"{self.room.name} | {self.checkin_at.date()} to {self.checkout_at.date()}"

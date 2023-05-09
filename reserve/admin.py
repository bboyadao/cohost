from django.contrib import admin
from django.core.exceptions import ValidationError
from rangefilter.filters import DateTimeRangeFilter

from reserve.models import Reserve, Room


class RoomFilter(DateTimeRangeFilter):
	def queryset(self, request, queryset):
		if self.form.is_valid():
			validated_data = dict(self.form.cleaned_data.items())
			if validated_data:
				time_in = validated_data.get("reserve__range__gte", None)
				time_out = validated_data.get("reserve__range__lte", None)
				if all([time_out, time_in]):
					if time_out < time_in:
						raise ValidationError(message="Checkout day must be greater than checkin day.")

					return Room.objects.available(time_in, time_out)
		return queryset


@admin.register(Room)
class ReserveAdmin(admin.ModelAdmin):
	list_display = ["name", ]

	list_filter = [
		("reserve", RoomFilter),
	]


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
	list_display = ["room", "checkin_at", "checkout_at", ]
	list_filter = ["checkin_at", "checkout_at", ]

from django_filters import rest_framework as filters
from advertisements.models import Advertisement
from django.contrib.auth import get_user_model

User = get_user_model()


class AdvertisementFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    creator = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ["created_at", "creator", "status"]

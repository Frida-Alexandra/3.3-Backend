from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from django_filters import rest_framework as filters
from .filters import AdvertisementFilter
from .permissions import IsAdvertisementOwner


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = filters.DjangoFilterBackend
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ["delete", "update", "partial_update"]:
            return [IsAuthenticated(), IsAdvertisementOwner()]
        return []

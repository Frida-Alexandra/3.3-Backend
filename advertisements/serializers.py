from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = (
            "id",
            "title",
            "description",
            "creator",
            "status",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user
        if not self.instance:
            if Advertisement.objects.filter(creator=user).count() > 10:
                raise serializers.ValidationError(
                    f"User {user} Ограничение до 10 объявлений!"
                )
        return data

    def update(self, instance, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().update(instance, validated_data)

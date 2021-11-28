from rest_framework import serializers

from src.accounts.models import UserProfile


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('id', 'date_joined', 'updated_on', 'user')

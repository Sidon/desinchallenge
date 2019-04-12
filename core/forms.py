from django.forms import ModelForm
import django_filters
from .models import Follower


class FollowerFilter(django_filters.FilterSet):
    class Meta:
        model = Follower
        fields = ('full_name',)


class FollowerForm(ModelForm):
    class Meta:
        model = Follower

        fields = ['id_instagram', 'user_name', 'profile_url', 'image_url', 'is_private', 'is_verified',
                  'followed_by_viewer']

id
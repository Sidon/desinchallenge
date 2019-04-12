from django.contrib import admin
from core.models import Follower


__author__ = "Sidon Duarte"
__date__ = "Created by 12/04/19"
__copyright__ = "Copyright 2019"
__email__ = "sidoncd@gmail.com"


LIST_PER_PAGE = 10

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['data_coleta','id_instagram', 'user_name', 'profile_url', 'full_name', 'image_url', 'is_private',
                    'is_verified', 'followed_by_viewer', 'data_insercao', 'data_atualizacao']
    list_display_links = list_display
    search_fields = ['id_instagram', 'user_name', 'full_name']
    list_filter = ['data_coleta', 'data_atualizacao', 'data_insercao', 'is_private']
    list_per_page = LIST_PER_PAGE


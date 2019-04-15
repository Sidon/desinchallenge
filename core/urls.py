import os
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
from desinchallenge import settings


app_name = 'core'
router = DefaultRouter()
router.register(r'followers', views.FollowerViewSet)


urlpatterns = [
    url(r'^$', views.FollowerListView.as_view(), name='home'),
    url('update-follower/(?P<pk>[\w-]+)$', views.FollowerUpdateView.as_view(), name='update1'),
    url(r'readme/', views.ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')},
        name='readme'),
    url(r'coleta/', views.ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'doc/get_csv.rst')},
        name='coleta')
]


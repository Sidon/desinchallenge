from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

router = DefaultRouter()

router.register(r'followers', views.FollowerViewSet)
# router.register(r'api/followers', views.FollowerViewSet)


urlpatterns = [
    url(r'^$', views.FollowerListView.as_view(), name='home'),
    url('update-follower/(?P<pk>[\w-]+)$', views.FollowerUpdateView.as_view(), name='update1'),
    url(r'filtro1', views.FilteredFollowerListView.as_view(), name='filter1'),
    url(r'readme/', views.ReadMeView.as_view(), name='readme'),

    # url(r'consultas/', views.ConsultaListView.as_view(), name='consultas'),
    # url(r'exames/', views.ExameListView.as_view(), name='exames'),
    # url('update-exame/(?P<pk>[\w-]+)$', views.ExameUpdateView.as_view(), name='update-exame'),
    #
    #

]



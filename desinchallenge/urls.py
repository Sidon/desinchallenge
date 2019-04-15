## desinchallenge URL Configuration

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from core.urls import router
schema_view = get_swagger_view(title='Desinchallenge API')


app_name = 'desinchallenge'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='api-token'),
    path('api/', include(router.urls)),
    path('', include('core.urls')),
    path('viewapi/', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

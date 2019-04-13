from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from core.models import Follower
from django.core.management import call_command


# Testa a inclusao dos dados iniciais
class ConsulTest(APITestCase):


    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_by_id(self):
        follower  = Follower.objects.get(id_instagram='1524004563')
        self.assertEqual(follower.user_name, 'sidonduarte')

    def test_get_by_username(self):
        follower  = Follower.objects.get(user_name='nataliavassalo')
        self.assertEqual(follower.id_instagram, '408388154')

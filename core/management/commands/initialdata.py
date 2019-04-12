import os
import math
import time
import pandas as pd
from django.core.management.base import BaseCommand
from core.models import Logdb, Follower
from django.contrib.auth.models import User
from django.db.models import Q
from util.logapi import Log_api
from desinchallenge import settings
from dateutil.parser import parse

def read_csv(file_name):
    fname = os.path.join(settings.DATA, file_name)
    try:
        return pd.read_csv(fname)
    except Exception as e:
        print("Erro ao abrir o arquivo: ", str(e))


class Command(BaseCommand):
    help = 'Create initial data'
    log_api = Log_api()

    def handle(self, *args, **options):
        if User.objects.filter(Q(username='admin') & Q(is_superuser=1)):

            start = time.time()
            followers = read_csv('followers_evolution.csv')

            Follower.objects.all().delete()
            Logdb.objects.all().delete()

            for _, row in followers.iterrows():
                follower = Follower()
                follower.id_instagram = row.id
                follower.user_name = row.username
                follower.profile_url = row.profileUrl
                follower.full_name = row.fullName
                follower.image_url = row.imgUrl
                if str(row.isVerified) != 'nan': follower.is_verified = row.isVerified
                if str(row.isPrivate) != 'nan': follower.is_private = row.isPrivate
                if str(row.followedByViewer) != 'nan': follower.followed_by_viewer = row.followedByViewer
                follower.data_coleta = parse(row.timestamp)

                follower.save()

                # Follower.objects.create(
                #    id_instagram=row.id, user_name=row.username, profile_url=row.profileUrl, full_name=row.fullName,
                #    image_url=row.imgUrl, is_private=row.isPrivate, is_verified=row.isVerified,
                #    followed_by_viewer=row.followedByViewer, data_coleta=parse(row.timestamp))
            else:
                print('Tempo gasto na operação:',(time.time() - start)/60, 'minutos')

        else:
            print('Inclua um usuário superuser com o nome admin')









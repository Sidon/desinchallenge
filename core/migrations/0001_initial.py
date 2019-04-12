# Generated by Django 2.2 on 2019-04-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_instagram', models.IntegerField(unique=True, verbose_name='Id Instagram')),
                ('user_name', models.CharField(max_length=70, verbose_name='Username')),
                ('profile_url', models.URLField(verbose_name='Profile URL')),
                ('full_name', models.CharField(max_length=70, verbose_name='Nome completo')),
                ('image_url', models.URLField(verbose_name='Url da imagem')),
                ('is_private', models.CharField(blank=True, max_length=10, null=True, verbose_name='Privacidade')),
                ('is_verified', models.CharField(blank=True, max_length=10, null=True, verbose_name='Verificação')),
                ('followed_by_viewer', models.CharField(blank=True, max_length=10, null=True, verbose_name='Followed')),
                ('data_coleta', models.DateTimeField(verbose_name='Data da coleta')),
                ('data_insercao', models.DateTimeField(auto_now_add=True, verbose_name='Data da inserção')),
                ('data_atualizaçãp', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
            ],
        ),
        migrations.CreateModel(
            name='Logdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_req', models.TextField(verbose_name='Post to API, via request (Python)')),
                ('post_curl', models.TextField(verbose_name='Post to API, via curl (CLI)')),
            ],
            options={
                'verbose_name': 'Log Post',
                'verbose_name_plural': 'Logs Posts',
            },
        ),
    ]

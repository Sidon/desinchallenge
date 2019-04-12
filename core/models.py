from django.db import models

# Create your models here.

bnull = dict(blank=True, null=True)

class Follower(models.Model):
    id_instagram = models.IntegerField('Id Instagram', unique=True)
    user_name = models.CharField('Username', max_length=70)
    profile_url = models.URLField('Profile URL')
    full_name = models.CharField('Nome completo', max_length=70)
    image_url = models.URLField('Url da imagem')
    is_private = models.CharField('Privacidade', max_length=10, **bnull)
    is_verified = models.CharField('Verificação', max_length=10, **bnull)
    followed_by_viewer = models.CharField('Followed', max_length=10, **bnull)
    data_coleta = models.DateTimeField('Data da coleta',auto_now=False)
    data_insercao = models.DateTimeField('Data da inserção', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Última atualização', auto_now=True)

    def __str__(self):
        return self.user_name


class Logdb(models.Model):
    post_req = models.TextField(verbose_name='Post to API, via request (Python)')
    post_curl = models.TextField(verbose_name='Post to API, via curl (CLI)')

    class Meta:
        verbose_name = 'Log Post'
        verbose_name_plural = 'Logs Posts'





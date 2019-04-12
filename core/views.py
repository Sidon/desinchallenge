import os
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django_tables2 import RequestConfig
from django.core.exceptions import ValidationError
from rest_framework import authentication, permissions, viewsets, filters
from rest_framework_tracking.mixins import LoggingMixin
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_filters.rest_framework import DjangoFilterBackend
from desinchallenge import settings
from .models import Follower, Logdb
from .serializers import FolowerSerializer, TrackSerializer, LogdbSerializer
from .tables import FollowerTable, LogdbTable
from .forms import FollowerForm, FollowerFilter

class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""

    authentication_classes = (
         authentication.BasicAuthentication,
         authentication.TokenAuthentication,
    )
    permission_classes = (
         permissions.IsAuthenticated,
    )

    # authentication_classes = ()
    # permission_classes = ()

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class FollowerListView(ListView):
    model = Follower
    template_name = 'core/follower_list.html'
    context_object_name = 'Follower'

    def get_context_data(self, **kwargs):
        context = super(FollowerListView, self).get_context_data(**kwargs)
        table = FollowerTable(Follower.objects.all().order_by('full_name'))
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table
        return context


class FollowerCreateView(CreateView):
    model = Follower
    template_name = 'core/follower-create.html'
    form_class = FollowerForm
    success_url = '/consultas'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class FollowerUpdateView(UpdateView):
    model = Follower
    template_name = 'core/follower-create.html'
    form_class = FollowerForm
    success_url = '/consultas'

    def form_valid(self, form,):
        before = Follower.objects.filter(pk=self.object.id)[0]
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class ReadMeView(TemplateView):
    template_name = "core/readme.html"

    def get_context_data(self, **kwargs):
        rst_file = os.path.join(settings.BASE_DIR, 'README.rst')
        with open(rst_file, 'r') as f:
            text = f.read()

        print(text)
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['text'] = text

        return context


class FollowerUpdateView(UpdateView):
    model = Follower
    template_name = 'core/follower-create.html'
    form_class = FollowerForm
    success_url = '/home'

    def form_valid(self, form,):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class FilteredFollowerListView(SingleTableMixin, FilterView):
    table_class = FollowerTable
    model = Follower
    template_name = 'core/follower_list.html'
    filterset_class = FollowerFilter

    def get_table_data(self):
        f = FollowerFilter(self.request.GET, queryset=Follower.objects.all().order_by('full_name'), request=self.request)
        return f

    def get_context_data(self, **kwargs):
        context = super(FilteredFollowerListView, self).get_context_data(**kwargs)
        f = FollowerFilter(self.request.GET, queryset=Follower.objects.all().order_by('full_name'), request=self.request)
        context['form'] = f.form
        return context

    #     # table = FollowerTable(Follower.objects.all().order_by('full_name'))
    #     RequestConfig(self.request, ).configure(table)
    #     # context['table'] = table
    #     return context


class FollowerViewSet(DefaultsMixin, LoggingMixin, viewsets.ModelViewSet):
    serializer_class = FolowerSerializer
    search_fields = ('full_name' )
    queryset = Follower.objects.all()

    def get_queryset(self):
        queryset = Follower.objects.all()
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)
        empty = self.request.query_params.get('empty', None)

        # Filtrando por privacidade
        is_private = self.request.query_params.get('is_private', None)

        if empty is not None:
            try:
                Follower.objects.all().delete()
                raise ValidationError('Empty Ok')
            except Exception as e:
                print(e)

        return queryset

    def _perform(self, anterior):
        self.request.query_params._mutable = True
        self.request.query_params['user'] = self.request.user

        return  {"user_id": str(self.request.user), "id_instagram": self.request.POST.get("id_instagram"),
                "dados_atual": self.request.POST.get("dados_Consulta"),
                "dados_anterior": anterior}



from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_app import models
from rest_framework.pagination import PageNumberPagination


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
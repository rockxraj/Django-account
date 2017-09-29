from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from .serializers import AccountSerializer, UserSerializer
from .models import Account
from .authentication import LoginAuthentication

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['post']

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name','last_name', 'branch',)
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )   

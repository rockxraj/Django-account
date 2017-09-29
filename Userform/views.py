from rest_framework import viewsets
from .serializers import UserformSerializer
from .models import Userform

class UserformViewSet(viewsets.ModelViewSet):
    queryset = Userform.objects.all()
    serializer_class = UserformSerializer

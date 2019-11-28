from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.quickstart.serializers import UserSerializer, MascotaSerializer
from blog.models import Mascotas

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Mascotas.objects.all()
    serializer_class = MascotaSerializer


from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Usuario,Mascotas

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class MascotaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mascotas
        fields = ('foto','nombre','raza','descripcion','estado')

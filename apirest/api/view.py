from rest_framework.viewsets import ModelViewSet
from apirest.models import *
from apirest.api.serializer import PostSerealizer

class PostApiViewSet(ModelViewSet):
    serializer_class=PostSerealizer
    queryset=propietario.objects.all()

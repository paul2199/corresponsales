from rest_framework.serializers import ModelSerializer
from apirest.models import propietario

class PostSerealizer(ModelSerializer):
    class Meta:
        model = propietario
        field =['id','cedula','nombre']
        depth=3
        fields='__all__'
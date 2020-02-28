from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Hospital, Medico, Paciente


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

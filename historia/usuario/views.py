from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from historia.usuario.serializers import HospitalSerializer, MedicoSerializer, PacienteSerializer
from .models import Hospital, Medico, Paciente


class HospitalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

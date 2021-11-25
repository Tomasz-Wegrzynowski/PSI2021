from .models import Klient, Samochod, Wypozyczenie
from .serializers import KlientSerializer, SamochodSerializer, WypozyczenieSerializer
from rest_framework import generics
#from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Witaj, prosty widok dla wypozyczalnia")

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


class SamochodList(generics.ListCreateAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-list'


class SamochodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-detail'


class WypozyczenieList(generics.ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    name = 'wypozyczenie-list'


class WypozyczenieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    name = 'wypozyczenie-detail'
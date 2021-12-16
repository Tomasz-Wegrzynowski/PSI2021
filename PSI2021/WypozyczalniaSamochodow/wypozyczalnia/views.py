from .models import Klient, Samochod, Wypozyczenie
from .serializers import KlientSerializer, SamochodSerializer, WypozyczenieSerializer, UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from django.contrib.auth.models import User
from rest_framework import permissions
from .custompermission import IsCurrentUserOwnerOrReadOnly
#from django.http import HttpResponse

# Create your views here.


class RootApi(generics.GenericAPIView):
    name = 'root-api'

    def get(self, request, *args, **kwargs):
        return Response({
            'klienci': reverse(KlientList.name, request=request),
            'samochody': reverse(SamochodList.name, request=request),
            'wypozyczenia': reverse(WypozyczenieList.name, request=request),
            'użytkownicy': reverse(UserList.name, request=request),
        })


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'
    filter_fields = ['imie', 'nazwisko', 'pesel']
    search_fields = ['imie', 'nazwisko', 'pesel']
    ordering_fields = ['imie', 'nazwisko', 'pesel']


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


class SamochodFilter(FilterSet):
    from_number_doors = NumberFilter(field_name='liczbaDrzwi', lookup_expr='gte')
    to_number_doors = NumberFilter(field_name='liczbaDrzwi', lookup_expr='lte')
    from_number_places = NumberFilter(field_name='liczbaMiejsc', lookup_expr='gte')
    to_number_places = NumberFilter(field_name='liczbaMiejsc', lookup_expr='lte')

    class Meta:
        model = Samochod
        fields = ['from_number_doors', 'to_number_doors', 'from_number_places', 'to_number_places']


class SamochodList(generics.ListCreateAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-list'
    filter_class = SamochodFilter
    search_fields = ['numerRejestracyjny', 'marka', 'typ', 'kolor']
    ordering_fields = ['numerRejestracyjny', 'marka']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SamochodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)


class WypozyczenieFilter(FilterSet):
    from_date = DateTimeFilter(field_name='dataStartu', lookup_expr='gte')
    to_date = DateTimeFilter(field_name='dataKonca', lookup_expr='lte')

    class Meta:
        model = Wypozyczenie
        fields = ['from_date', 'to_date']


class WypozyczenieList(generics.ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    name = 'wypozyczenie-list'
    filter_class = WypozyczenieFilter
    search_fields = ['klient', 'samochod', 'MiejsceOdbioruSamochodu', 'MiejsceZwrotuSamochodu']
    ordering_fields = ['klient', 'samochod', 'MiejsceOdbioruSamochodu', 'MiejsceZwrotuSamochodu']


class WypozyczenieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    name = 'wypozyczenie-detail'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
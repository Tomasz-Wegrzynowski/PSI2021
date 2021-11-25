from rest_framework import serializers
from .models import Klient, Samochod, Wypozyczenie


class SamochodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samochod
        fields = ['idSamochodu', 'numerRejestracyjny', 'marka', 'typ', 'kolor', 'liczbaMiejsc', 'liczbaDrzwi', 'typPaliwa', 'typSkrzyniBiegow', 'uszkodzenia']


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['pesel', 'imie', 'nazwisko', 'kategoriaPrawajazdy', 'numerTelefonu', 'email']

class WypozyczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = ['idWypozyczenia', 'dataStartu', 'dataKonca', 'MiejsceOdbioruSamochodu', 'MiejsceZwrotuSamochodu', 'canaWypozyczenia', 'klient', 'samochod']

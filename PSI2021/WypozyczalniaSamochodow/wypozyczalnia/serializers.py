from rest_framework import serializers
from .models import Klient, Samochod, Wypozyczenie
from django.contrib.auth.models import User


class SamochodSerializer(serializers.HyperlinkedModelSerializer):
    wypozyczenia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='wypozyczenie-detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Samochod
        fields = ['url', 'idSamochodu', 'numerRejestracyjny', 'marka', 'typ', 'kolor', 'liczbaMiejsc', 'liczbaDrzwi', 'typPaliwa', 'typSkrzyniBiegow', 'uszkodzenia', 'wypozyczenia', 'owner']

    def validate_liczbaMiejsc(self, value):
        if value <= 0:
            raise serializers.ValidationError("Liczba miejsc musi być wieksza niż 0", )
        return value

    def validate_liczbaDrzwi(self, value):
        if value <= 0:
            raise serializers.ValidationError("Liczba drzwi musi być wieksza niż 0", )
        return value


class KlientSerializer(serializers.HyperlinkedModelSerializer):
    wypozyczenia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='wypozyczenie-detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Klient
        fields = ['url', 'pesel', 'imie', 'nazwisko', 'kategoriaPrawajazdy', 'numerTelefonu', 'email', 'wypozyczenia', 'owner']


class WypozyczenieSerializer(serializers.HyperlinkedModelSerializer):
    klient = serializers.SlugRelatedField(queryset=Klient.objects.all(), slug_field='nazwisko')
    samochod = serializers.SlugRelatedField(queryset=Samochod.objects.all(), slug_field='marka')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Wypozyczenie
        fields = ['url', 'idWypozyczenia', 'dataStartu', 'dataKonca', 'MiejsceOdbioruSamochodu', 'MiejsceZwrotuSamochodu', 'canaWypozyczenia', 'klient', 'samochod', 'owner']

    def validate_canaWypozyczenia(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena musi być równa lub większa od 0", )
        return value


class UserSamochodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Samochod
        fields = ['url','numerRejestracyjny']


class UserKlientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Klient
        fields = ['url', 'nazwisko']

class UserWypozyczenieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = ['url', 'idWypozyczenia']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    samochody = UserSamochodSerializer(many=True,read_only=True)
    klienci = UserKlientSerializer(many=True, read_only=True)
    wypozyczenia = UserWypozyczenieSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'samochody', 'klienci', 'wypozyczenia']
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User
from .models import Klient, Samochod


class KlientTests(APITestCase):
    def create_klient(self, pesel, imie, nazwisko, kategoriaPrawajazdy, numerTelefonu, email, client):
        url = reverse(views.KlientList.name)
        data = {'pesel': pesel,
                'imie': imie,
                'nazwisko': nazwisko,
                'kategoriaPrawajazdy': kategoriaPrawajazdy,
                'numerTelefonu': numerTelefonu,
                'email': email}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_klient(self):
        User.objects.create_superuser('admin', 'admin@ad.com', '1234')
        client = APIClient()
        client.login(username='admin', password='1234')
        new_pesel = '17231232122'
        new_imie = 'Jakub'
        new_nazwisko = 'Szczepański'
        new_kategoriaPrawajazdy = 'B'
        new_numerTelefonu = '777888111'
        new_email = 'jakub@wp.pl'
        response = self.create_klient(new_pesel, new_imie, new_nazwisko, new_kategoriaPrawajazdy, new_numerTelefonu, new_email, client)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert Klient.objects.count() == 1
        assert Klient.objects.get().imie == new_imie
        assert Klient.objects.get().nazwisko == new_nazwisko

    def test_post_existing_klient(self):
        User.objects.create_superuser('admin', 'admin@ad.com', '1234')
        client = APIClient()
        client.login(username='admin', password='1234')
        new_pesel = '17231232122'
        new_imie = 'Jakub'
        new_nazwisko = 'Szczepański'
        new_kategoriaPrawajazdy = 'B'
        new_numerTelefonu = '777888111'
        new_email = 'jakub@wp.pl'
        response_one = self.create_klient(new_pesel, new_imie, new_nazwisko, new_kategoriaPrawajazdy, new_numerTelefonu, new_email, client)
        response_two = self.create_klient(new_pesel, new_imie, new_nazwisko, new_kategoriaPrawajazdy, new_numerTelefonu, new_email, client)
        self.assertEqual(response_one.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_two.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_klient(self):
        User.objects.create_superuser('admin', 'admin@ad.com', '1234')
        client = APIClient()
        client.login(username='admin', password='1234')
        new_pesel = '17231232122'
        new_imie = 'Jakub'
        new_nazwisko = 'Szczepański'
        new_kategoriaPrawajazdy = 'B'
        new_numerTelefonu = '777888111'
        new_email = 'jakub@wp.pl'
        response = self.create_klient(new_pesel, new_imie, new_nazwisko, new_kategoriaPrawajazdy, new_numerTelefonu, new_email, client)
        url = urls.reverse(views.KlientDetail.name, None, {response.data['pesel']})
        updated_imie = 'Adam'
        data = {'pesel': new_pesel,
                'imie': updated_imie,
                'nazwisko': new_nazwisko,
                'kategoriaPrawajazdy': new_kategoriaPrawajazdy,
                'numerTelefonu': new_numerTelefonu,
                'email': new_email}
        patch_response = client.patch(url, data, format='json')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        assert patch_response.data['imie'] == updated_imie


class SamochodTests(APITestCase):
    def create_samochod(self, numerRejestracyjny, marka, typ, kolor,
                        liczbaMiejsc, liczbaDzrwi, typPaliwa, typSkrzyniBiegow,
                        uszkodzenia, client):
        url = reverse(views.SamochodList.name)
        data = {'numerRejestracyjny': numerRejestracyjny,
                'marka': marka,
                'typ': typ,
                'kolor': kolor,
                'liczbaMiejsc': liczbaMiejsc,
                'liczbaDrzwi': liczbaDzrwi,
                'typPaliwa': typPaliwa,
                'typSkrzyniBiegow': typSkrzyniBiegow,
                'uszkodzenia': uszkodzenia}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_samochod(self):
        User.objects.create_superuser('admin', 'admin@ad.com', '1234')
        client = APIClient()
        client.login(username='admin', password='1234')
        new_numerRejestracyjny = 'NO9012'
        new_marka = 'Audi'
        new_typ = 'Sedan'
        new_kolor = 'Niebieski'
        new_liczbaMiejsc = '2'
        new_liczbaDrzwi = '3'
        new_typPaliwa = 'Benzyna'
        new_typSkrzyniBiegow = 'Manualna'
        new_uszkodzenia = 'Brak'
        response = self.create_samochod(new_numerRejestracyjny, new_marka, new_typ, new_kolor, new_liczbaMiejsc,
                                      new_liczbaDrzwi, new_typPaliwa, new_typSkrzyniBiegow, new_uszkodzenia, client)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert Samochod.objects.count() == 1
        assert Samochod.objects.get().numerRejestracyjny == new_numerRejestracyjny
        assert Samochod.objects.get().marka == new_marka

    def test_post_existing_samochod(self):
        User.objects.create_superuser('admin', 'admin@ad.com', '1234')
        client = APIClient()
        client.login(username='admin', password='1234')
        new_numerRejestracyjny = 'NO9012'
        new_marka = 'Audi'
        new_typ = 'Sedan'
        new_kolor = 'Niebieski'
        new_liczbaMiejsc = '2'
        new_liczbaDrzwi = '3'
        new_typPaliwa = 'Benzyna'
        new_typSkrzyniBiegow = 'Manualna'
        new_uszkodzenia = 'Brak'
        response_one = self.create_samochod(new_numerRejestracyjny, new_marka, new_typ, new_kolor, new_liczbaMiejsc,
                                      new_liczbaDrzwi, new_typPaliwa, new_typSkrzyniBiegow, new_uszkodzenia, client)
        response_two = self.create_samochod(new_numerRejestracyjny, new_marka, new_typ, new_kolor, new_liczbaMiejsc,
                                      new_liczbaDrzwi, new_typPaliwa, new_typSkrzyniBiegow, new_uszkodzenia, client)
        self.assertEqual(response_one.status_code, status.HTTP_201_CREATED)
        assert Samochod.objects.count() == 1
        self.assertEqual(response_two.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_samochod(self):
        User.objects.create_superuser('admin', 'admin@ad.com', '1234')
        client = APIClient()
        client.login(username='admin', password='1234')
        new_numerRejestracyjny = 'NO9012'
        new_marka = 'Audi'
        new_typ = 'Sedan'
        new_kolor = 'Niebieski'
        new_liczbaMiejsc = '2'
        new_liczbaDrzwi = '3'
        new_typPaliwa = 'Benzyna'
        new_typSkrzyniBiegow = 'Manualna'
        new_uszkodzenia = 'Brak'
        response = self.create_samochod(new_numerRejestracyjny, new_marka, new_typ, new_kolor, new_liczbaMiejsc,
                                        new_liczbaDrzwi, new_typPaliwa, new_typSkrzyniBiegow, new_uszkodzenia,
                                        client)
        url = urls.reverse(views.SamochodDetail.name, None, {response.data['idSamochodu']})
        updated_marka = 'Volvo'
        data = {'numerRejestracyjny': new_numerRejestracyjny,
                'marka': updated_marka,
                'typ': new_typ,
                'kolor': new_kolor,
                'liczbaMiejsc': new_liczbaMiejsc,
                'liczbaDrzwi': new_liczbaDrzwi,
                'typPaliwa': new_typPaliwa,
                'typSkrzyniBiegow': new_typSkrzyniBiegow,
                'uszkodzenia': new_uszkodzenia}
        patch_response = client.patch(url, data, format='json')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        assert patch_response.data['marka'] == updated_marka
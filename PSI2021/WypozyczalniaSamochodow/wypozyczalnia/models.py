from django.db import models

# Create your models here.


class Klient(models.Model):
    pesel = models.CharField(max_length=11, primary_key=True)
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=60)
    kategoriaPrawajazdy = models.CharField(max_length=20)
    numerTelefonu = models.CharField(max_length=11)
    email = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.imie + " " + self.nazwisko


class Samochod(models.Model):
    idSamochodu = models.AutoField(primary_key=True)
    numerRejestracyjny = models.CharField(max_length=10)
    marka = models.CharField(max_length=45)
    typ = models.CharField(max_length=45)
    kolor = models.CharField(max_length=45, null=True)
    liczbaMiejsc = models.IntegerField()
    liczbaDrzwi = models.IntegerField()
    typPaliwa = models.CharField(max_length=45)
    typSkrzyniBiegow = models.CharField(max_length=45)
    uszkodzenia = models.TextField(null=True)

    def __str__(self):
        return self.marka


class Wypozyczenie(models.Model):
    idWypozyczenia = models.AutoField(primary_key=True)
    dataStartu = models.DateTimeField()
    dataKonca = models.DateTimeField()
    MiejsceOdbioruSamochodu = models.CharField(max_length=100)
    MiejsceZwrotuSamochodu = models.CharField(max_length=100)
    canaWypozyczenia = models.DecimalField(max_digits=10, decimal_places=2)
    klient = models.ForeignKey(Klient, related_name='wypozyczenia', on_delete=models.SET_NULL, null=True)
    samochod = models.ForeignKey(Samochod, related_name='wypozyczenia', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.idWypozyczenia + " " + self.dataStartu + " " + self.dataKonca

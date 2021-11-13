from django.contrib import admin
from .models import Wypozyczenie, Klient, Samochod
# Register your models here.

admin.site.register(Klient)
admin.site.register(Samochod)
admin.site.register(Wypozyczenie)

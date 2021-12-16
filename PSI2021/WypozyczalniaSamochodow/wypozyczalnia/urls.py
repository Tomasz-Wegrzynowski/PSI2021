from django.urls import path

from . import views

urlpatterns = [
    path('klient/', views.KlientList.as_view(), name=views.KlientList.name),
    path('klient/<int:pk>', views.KlientDetail.as_view(), name=views.KlientDetail.name),
    path('samochod/', views.SamochodList.as_view(), name=views.SamochodList.name),
    path('samochod/<int:pk>', views.SamochodDetail.as_view(), name=views.SamochodDetail.name),
    path('wypozyczenie/', views.WypozyczenieList.as_view(), name=views.WypozyczenieList.name),
    path('wypozyczenie/<int:pk>', views.WypozyczenieDetail.as_view(), name=views.WypozyczenieDetail.name),
    path('uzytkownicy', views.UserList.as_view(), name=views.UserList.name),
    path('uzytkownicy/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.RootApi.as_view(), name=views.RootApi.name),

]
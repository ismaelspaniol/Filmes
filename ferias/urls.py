from django.urls import path
from .views import listagem


app_name='ferias'

urlpatterns = [
    path('listagem/', listagem, name="listagem"),


]
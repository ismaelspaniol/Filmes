from django.urls import path
from musicas.views import musica_new, musicas_delete, musicas_list, musicas_update

app_name = 'musicas'

urlpatterns = [
    path('new/', musica_new, name="musica_new"),
    path('list/', musicas_list, name="musicas_list"),
    path('update/<int:id>/', musicas_update, name="musicas_update"),
    path('delete/<int:id>/', musicas_delete, name="musicas_delete"),
    ]



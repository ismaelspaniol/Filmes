from django.urls import path
from .views import filme_new, filmes_list, filmes_delete, filmes_update

app_name = 'movies'

urlpatterns = [
    path('new/', filme_new, name="filme_new"),
    path('list/', filmes_list, name="filmes_list"),
    path('update/<int:id>/', filmes_update, name="filmes_update"),
    path('delete/<int:id>/', filmes_delete, name="filmes_delete"),
    ]
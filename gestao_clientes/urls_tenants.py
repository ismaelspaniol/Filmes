from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(home_urls)),
    path('clientes/', include('clientes.urls',  namespace='clientes')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('ferias/', include('ferias.urls', namespace='ferias')),
    path('movies/', include('movies.urls', namespace='movies')),
    path('musicas/', include('musicas.urls', namespace='musicas')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





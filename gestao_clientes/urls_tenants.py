from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from django.contrib.auth import views as auth_views
from customers.views import TenantView

urlpatterns = [
    # path('', include(home_urls)),
    path('', TenantView.as_view()),
    path('clientes/', include('clientes.urls',  namespace='clientes')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('ferias/', include('ferias.urls', namespace='ferias')),

]





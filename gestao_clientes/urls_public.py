from customers.views import TenantView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', TenantView.as_view()),
    path('admin/', admin.site.urls),
]

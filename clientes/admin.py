from django.contrib import admin
from .models import Person
from .models import Documento, Dependente


admin.site.register(Person)
admin.site.register(Documento)
admin.site.register(Dependente)
# Register your models here.

from django.contrib.auth.models import User
from django.db.utils import DatabaseError
from django.views.generic import FormView
from customers.forms import GenerateUsersForm
from customers.models import Client
from random import choice



class TenantView(FormView):
    form_class = GenerateUsersForm
    template_name = 'index_tenant.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tenants_list'] = Client.objects.all()
        context['users'] = User.objects.all()
        return context


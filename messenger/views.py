from django.shortcuts import render
from django.views import View
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MessengerView(LoginRequiredMixin,View):
    login_url = '/account/login/'
    redirect_field_name = '/'
    template_name = 'messenger\messenger.html'
    def get(self, request, **kwargs):
        stock=Message.objects.all().order_by('-id')[:50]
        print('tere',stock)
        print('dscsdc',Message.objects.all().order_by('id'))
        return render(request, self.template_name,{'stock':stock})
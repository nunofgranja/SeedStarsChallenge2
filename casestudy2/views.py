from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView

from .models import Entity


class IndexView(TemplateView):
    template_name = 'casestudy2/index.html';

class ListView(generic.ListView):
    template_name= 'casestudy2/list.html'
    def get_queryset(self):
        return Entity.objects.order_by('entity_name')

class AddView(TemplateView):
    template_name = 'casestudy2/add.html';

def addentity(request):
    e = Entity(entity_name=request.POST['entity_name'],entity_email=request.POST['entity_email'])
    e.save();
    return HttpResponseRedirect(reverse('casestudy2:list'))

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from shortcuts.models import Shortcut
from shortcuts.forms import ShortcutForm

from rest_framework import viewsets
from .serializers import ShortcutSerializer

class ShortcutList(LoginRequiredMixin, ListView):
    model = Shortcut

class ShortcutView(DetailView):
    model = Shortcut

# class ShortcutCreate(CreateView):
#     model = Shortcut
#     fields = ['title_fi', 'content_fi', 'lang']
#     success_url = reverse_lazy('shortcut_list')

def index(request):
    # Generate counts of some of the main objects
    num_shortcuts = Shortcut.objects.all().count()
        
    context = {
        'num_shortcuts': num_shortcuts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def shortcut_update(request, pk, template_name='shortcuts/shortcut_update.html'):
    shortcut = get_object_or_404(Shortcut, pk=pk)
    form = ShortcutForm(request.POST or None, instance=shortcut)
    if form.is_valid():
        form.save()
        return redirect('shortcut_list')
    return render(request, template_name, {'form':form})

class ShortcutDelete(DeleteView):
    model = Shortcut
    success_url = reverse_lazy('shortcut_list')

class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all().order_by('title_fi')
    serializer_class = ShortcutSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from pages.models import Page
from pages.forms import PageForm

from rest_framework import viewsets
from .serializers import PageSerializer

class PageList(LoginRequiredMixin, ListView):
    model = Page

class PageView(DetailView):
    model = Page
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_list'] = Page.objects.all()
        return context

class PageCreate(CreateView):
    model = Page
    fields = ['title_fi', 'content_fi', 'lang']
    success_url = reverse_lazy('page_list')

def index(request):
    # Generate counts of some of the main objects
    num_pages = Page.objects.all().count()
        
    context = {
        'num_pages': num_pages,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def page_update(request, pk, template_name='pages/page_update.html'):
    page = get_object_or_404(Page, pk=pk)
    form = PageForm(request.POST or None, instance=page)
    if form.is_valid():
        form.save()
        return redirect('page_list')
    return render(request, template_name, {'form':form})

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('page_list')

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all().order_by('title_fi')
    serializer_class = PageSerializer
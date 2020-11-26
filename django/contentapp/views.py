import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page, Shortcut, SingleFigure, Figure
from .forms import PageForm, ShortcutForm, SingleFigureForm
from rest_framework import viewsets
from .serializers import PageSerializer, ShortcutSerializer, SingleFigureSerializer
from django.db.models import Max, Min

class PageList(LoginRequiredMixin, ListView):
  model = Page
  template_name = 'page_list.html'

class PageView(DetailView):
  model = Page
  template_name = 'page_detail.html'
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

def page_update(request, pk, template_name='page_update.html'):
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

from rest_framework import viewsets
from .serializers import ShortcutSerializer

class ShortcutList(LoginRequiredMixin, ListView):
  model = Shortcut
  template_name = 'shortcut_list.html'

class ShortcutView(DetailView):
  model = Shortcut
  template_name = 'shortcut_detail.html'

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

def shortcut_update(request, pk, template_name='shortcut_update.html'):
  shortcut = get_object_or_404(Shortcut, pk=pk)
  form = ShortcutForm(request.POST or None, request.FILES or None, instance=shortcut)

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


# Figures
class SingleFigureList(LoginRequiredMixin, ListView):
  model = SingleFigure
  context_object_name = 'figure_list'
  template_name = 'figure_list.html'
  queryset = SingleFigure.objects.all()

  def get_context_data(self, **kwargs):
    context = super(SingleFigureList, self).get_context_data(**kwargs)
    context['parents'] = Figure.objects.all()
    return context

  # Enable drag & drop position change
  def post(self, request):
    template_name = 'figure_list.html'
    current = json.loads(request.body)['current']
    new = json.loads(request.body)['new']
    SingleFigure.objects.get(pk=current).to(int(new))
    return render(request, template_name)

class SingleFigureView(DetailView):
  model = SingleFigure
  template_name = 'figure_detail.html'

def figure_add(request, template_name='figure_add.html'):
  form = SingleFigureForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('figure_list')
  return render(request, template_name, {'form':form})

def figure_update(request, pk, template_name='figure_update.html'):
  figure = get_object_or_404(SingleFigure, pk=pk)
  form = SingleFigureForm(request.POST or None, request.FILES or None, instance=figure)
  current = request.POST.get('figure')
  figure_parent = figure.figure.pk

  if form.is_valid():
    form.save(commit=False)
    # Move updated item to bottom if parent changes
    if int(figure_parent) != int(current):
      if SingleFigure.objects.filter(figure=current).aggregate(Max('placement_id'))['placement_id__max']:
        figure.placement_id = SingleFigure.objects.filter(figure=current).aggregate(Max('placement_id'))['placement_id__max'] + 1
      else:
        figure.placement_id = 1
    form.save()

    # Move items up to preserve concurrent placement id's
    for parent in Figure.objects.filter():
      if SingleFigure.objects.filter(figure=parent.pk):
        min_placement = SingleFigure.objects.filter(figure=parent.pk).aggregate(Min('placement_id'))['placement_id__min']
        if min_placement > 1:
          SingleFigure.objects.get(figure=parent.pk, placement_id=min_placement).to(1)
          for f in SingleFigure.objects.filter(figure=parent.pk):
            if SingleFigure.objects.get(figure=parent.pk, placement_id=f.placement_id).placement_id > 1:
              SingleFigure.objects.get(figure=parent.pk, placement_id=f.placement_id).up()

        # Move items up if empty space
        if SingleFigure.objects.filter(figure=parent.pk).count() > 1:
          object_count = SingleFigure.objects.filter(figure=parent.pk).count()
          for f in SingleFigure.objects.filter(figure=parent.pk):
            if SingleFigure.objects.filter(figure=parent.pk, placement_id=f.placement_id):
              next_fig = SingleFigure.objects.get(figure=parent.pk, placement_id=f.placement_id).next()
              if next_fig and (not SingleFigure.objects.filter(figure=parent.pk, placement_id=f.placement_id + 1)):
                for index, movable in enumerate(SingleFigure.objects.filter(figure=parent.pk, placement_id__gt=f.placement_id)):
                  SingleFigure.objects.get(figure=parent.pk, placement_id=movable.placement_id).to(f.placement_id + (index + 1))

    return redirect('figure_list')
  return render(request, template_name, {'form':form})

class FigureDelete(LoginRequiredMixin, DeleteView):
  model = SingleFigure
  template_name = 'figure_delete.html'
  success_url = reverse_lazy('figure_list')

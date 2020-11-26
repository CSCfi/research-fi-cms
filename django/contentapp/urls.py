from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
  path('pages/', views.PageList.as_view(), name='page_list'),
  path('pages/view/<int:pk>', views.PageView.as_view(), name='page_view'),
  path('pages/edit/<int:pk>', views.page_update, name='page_edit'),
  path('pages/delete/<int:pk>', views.PageDelete.as_view(), name='page_delete'),
  path('shortcuts/', views.ShortcutList.as_view(), name='shortcut_list'),
  path('shortcuts/view/<int:pk>', views.ShortcutView.as_view(), name='shortcut_view'),
  path('shortcuts/edit/<int:pk>', views.shortcut_update, name='shortcut_edit'),
  path('shortcuts/delete/<int:pk>', views.ShortcutDelete.as_view(), name='shortcut_delete'),
  path('figures/', views.SingleFigureList.as_view(), name='figure_list'),
  path('figures/view/<int:pk>', views.SingleFigureView.as_view(), name='figure_view'),
  path('figures/edit/<int:pk>', views.figure_update, name='figure_edit'),
  path('figures/add/', views.figure_add, name='figure_add'),
  path('figures/delete/<int:pk>', views.FigureDelete.as_view(), name='figure_delete'),
  path('sectors/', views.SectorList.as_view(), name='sector_list'),
  path('sectors/edit/<int:pk>', views.sector_update, name='sector_edit'),
  path('organizations/', views.OrganizationList.as_view(), name='organization_list'),
  path('organizations/edit/<int:pk>', views.organization_update, name='organization_edit'),
]
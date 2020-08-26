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
]
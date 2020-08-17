from django.urls import path

from shortcuts import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ShortcutList.as_view(), name='shortcut_list'),
    path('view/<int:pk>', views.ShortcutView.as_view(), name='shortcut_view'),
    path('edit/<int:pk>', views.shortcut_update, name='shortcut_edit'),
    path('delete/<int:pk>', views.ShortcutDelete.as_view(), name='shortcut_delete'),
]
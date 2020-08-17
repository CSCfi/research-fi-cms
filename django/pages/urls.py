from django.urls import path, include
from rest_framework import routers
from pages import views

urlpatterns = [
    path('', views.PageList.as_view(), name='page_list'),
    path('view/<int:pk>', views.PageView.as_view(), name='page_view'),
    path('edit/<int:pk>', views.page_update, name='page_edit'),
    path('delete/<int:pk>', views.PageDelete.as_view(), name='page_delete'),
]
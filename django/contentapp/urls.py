from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("pages/", views.PageList.as_view(), name="page_list"),
    path("pages/view/<int:pk>", views.PageView.as_view(), name="page_view"),
    path("pages/edit/<int:pk>", views.page_update, name="page_edit"),
    path("shortcuts/", views.ShortcutList.as_view(), name="shortcut_list"),
    path("shortcuts/view/<int:pk>", views.ShortcutView.as_view(), name="shortcut_view"),
    path("shortcuts/edit/<int:pk>", views.shortcut_update, name="shortcut_edit"),
    path("figures/", views.SingleFigureList.as_view(), name="figure_list"),
    path("figures/view/<int:pk>", views.SingleFigureView.as_view(), name="figure_view"),
    path("figures/edit/<int:pk>", views.figure_update, name="figure_edit"),
    path("figures/add/", views.figure_add, name="figure_add"),
    path("figures/delete/<int:pk>", views.FigureDelete.as_view(), name="figure_delete"),
    path("sectors/", views.SectorList.as_view(), name="sector_list"),
    path("sectors/edit/<int:pk>", views.sector_update, name="sector_edit"),
    path("organizations/", views.OrganizationList.as_view(), name="organization_list"),
    path(
        "organizations/edit/<int:pk>",
        views.organization_update,
        name="organization_edit",
    ),
    path("external-links/", views.OtherLinkList.as_view(), name="external_link_list"),
    path(
        "external-links/edit/<int:pk>",
        views.external_link_update,
        name="external_link_edit",
    ),
    path("external-links/add/", views.external_link_add, name="external_link_add"),
    path(
        "external-links/delete/<int:pk>",
        views.OtherLinkDelete.as_view(),
        name="external_link_delete",
    ),
]
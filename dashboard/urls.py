from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("charts/", views.charts, name="charts"),
    path("widgets/", views.widgets, name="widgets"),
    path("tables/", views.tables, name="tables"),
    path("grid/", views.grid, name="grid"),
    path("form-basic/", views.form_basic, name="form-basic"),
    path("form-wizard/", views.form_wizard, name="form-wizard"),
    path("buttons/", views.buttons, name="buttons"),
    path("icon-material/", views.icon_material, name="icon-material"),
    path("icon-fontawesome/", views.icon_fontawesome, name="icon-fontawesome"),
    path("elements/", views.elements, name="elements"),
    path("gallery/", views.gallery, name="gallery"),
    path("invoice/", views.invoice, name="invoice"),
    path("chat/", views.chat, name="chat"),
]
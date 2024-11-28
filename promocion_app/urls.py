from django.urls import path
from promocion_app import views

urlpatterns = [
    path('Promocion',views.inicio_vistaPromocion,name="Promocion"),
    path("registrarPromocion/",views.registrarPromocion,name="registrarPromocion"),
    path("seleccionarPromocion/<id_promocion>",views.seleccionarPromocion,name="seleccionarPromocion"),
    path("editarPromocion/",views.editarPromocion,name="editarPromocion"),
    path("borrarPromocion/<id_promocion>",views.borrarPromocion,name="borrarPromocion")
]
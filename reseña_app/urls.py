from django.urls import path
from reseña_app import views

urlpatterns = [
    path('Reseña',views.inicio_vistaReseña,name="Reseña"),
    path("registrarReseña/",views.registrarReseña,name="registrarReseña"),
    path("seleccionarReseña/<id_reseña>",views.seleccionarReseña,name="seleccionarReseña"),
    path("editarReseña/",views.editarReseña,name="editarReseña"),
    path("borrarReseña/<id_reseña>",views.borrarReseña,name="borrarReseña")
]
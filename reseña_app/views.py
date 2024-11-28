from django.shortcuts import render, redirect
from .models import Reseña

# Create your views here.

def inicio_vistaReseña(request):
    lasreseña=Reseña.objects.all()
    return render(request,'gestionarReseña.html',{'misreseña':lasreseña})

def registrarReseña(request):
    id_reseña=request.POST["numidreseña"]
    id_producto=request.POST["numidproducto"]
    id_cliente=request.POST["numidcliente"]
    calificacion=request.POST["numcalificacion"]
    comentario=request.POST["txtcomentario"]
    fecha_reseña=request.POST["txtfechareseña"]
    estado=request.POST["txtestado"]

    guardarreseña=Reseña.objects.create(id_reseña=id_reseña,id_producto=id_producto,id_cliente=id_cliente,calificacion=calificacion,comentario=comentario,fecha_reseña=fecha_reseña,estado=estado)

    return redirect('Reseña')

def seleccionarReseña(request,id_reseña):
    reseña=Reseña.objects.get(id_reseña=id_reseña)
    return render(request,"editarReseña.html",{"misreseña":reseña})

def editarReseña(request):
    id_reseña=request.POST["numidreseña"]
    id_producto=request.POST["numidproducto"]
    id_cliente=request.POST["numidcliente"]
    calificacion=request.POST["numcalificacion"]
    comentario=request.POST["txtcomentario"]
    fecha_reseña=request.POST["txtfechareseña"]
    estado=request.POST["txtestado"]

    reseña=Reseña.objects.get(id_reseña=id_reseña)

    reseña.id_producto=id_producto
    reseña.id_cliente=id_cliente
    reseña.calificacion=calificacion
    reseña.comentario=comentario
    reseña.fecha_reseña=fecha_reseña
    reseña.estado=estado
    reseña.save()

    return redirect('Reseña')

def borrarReseña(request,id_reseña):
    reseña=Reseña.objects.get(id_reseña=id_reseña)
    reseña.delete()

    return redirect('Reseña')
from django.shortcuts import render, redirect
from .models import Promocion

# Create your views here.

def inicio_vistaPromocion(request):
    laspromocion=Promocion.objects.all()
    return render(request,'gestionarPromocion.html',{'mispromocion':laspromocion})

def registrarPromocion(request):
    id_promocion=request.POST["numidpromocion"]
    descripcion=request.POST["txtdescripcion"]
    fecha_inicio=request.POST["txtfechainicio"]
    fecha_fin=request.POST["txtfechafin"]
    descuento=request.POST["numdescuento"]
    productos_aplicados=request.POST["numproductosaplicados"]
    condiciones=request.POST["txtcondiciones"]

    guardarpromocion=Promocion.objects.create(id_promocion=id_promocion,descripcion=descripcion,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,descuento=descuento,productos_aplicados=productos_aplicados,condiciones=condiciones)

    return redirect('Promocion')

def seleccionarPromocion(request,id_promocion):
    promocion=Promocion.objects.get(id_promocion=id_promocion)
    return render(request,"editarPromocion.html",{"mispromocion":promocion})

def editarPromocion(request):
    id_promocion=request.POST["numidpromocion"]
    descripcion=request.POST["txtdescripcion"]
    fecha_inicio=request.POST["txtfechainicio"] 
    fecha_fin=request.POST["txtfechafin"]
    descuento=request.POST["numdescuento"]
    productos_aplicados=request.POST["txtproductosaplicados"]
    condiciones=request.POST["txtcondiciones"]

    promocion=Promocion.objects.get(id_promocion=id_promocion)

    promocion.descripcion=descripcion
    promocion.fecha_inicio=fecha_inicio
    promocion.fecha_fin=fecha_fin
    promocion.descuento=descuento
    promocion.productos_aplicados=productos_aplicados
    promocion.condiciones=condiciones
    promocion.save()

    return redirect('Promocion')

def borrarPromocion(request,id_promocion):
    promocion=Promocion.objects.get(id_promocion=id_promocion)
    promocion.delete()

    return redirect('Promocion')
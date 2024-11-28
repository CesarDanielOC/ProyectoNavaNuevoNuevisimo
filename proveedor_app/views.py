from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.

def inicio_vistaProveedor(request):
    lasproveedor=Proveedor.objects.all()
    return render(request,'gestionarProveedor.html',{'misproveedor':lasproveedor})

def registrarProveedor(request):
    id_proveedor=request.POST["numidproveedor"]
    nombre_empresa=request.POST["txtnombreempresa"]
    contacto=request.POST["txtcontacto"]
    telefono=request.POST["numtelefono"]
    correo_electronico=request.POST["txtcorreoelectronico"]
    direccion=request.POST["txtdireccion"]

    guardarproveedor=Proveedor.objects.create(id_proveedor=id_proveedor,nombre_empresa=nombre_empresa,contacto=contacto,telefono=telefono,correo_electronico=correo_electronico,direccion=direccion)

    return redirect('Proveedor')

def seleccionarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarProveedor.html",{"misproveedor":proveedor})

def editarProveedor(request):
    id_proveedor=request.POST["numidproveedor"]
    nombre_empresa=request.POST["txtnombreempresa"]
    contacto=request.POST["txtcontacto"] 
    telefono=request.POST["numtelefono"]
    correo_electronico=request.POST["txtcorreoelectronico"]
    direccion=request.POST["txtdireccion"]


    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)

    proveedor.nombre_empresa=nombre_empresa
    proveedor.contacto=contacto
    proveedor.telefono=telefono
    proveedor.correo_electronico=correo_electronico
    proveedor.direccion=direccion
    proveedor.save()

    return redirect('Proveedor')

def borrarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()

    return redirect('Proveedor')
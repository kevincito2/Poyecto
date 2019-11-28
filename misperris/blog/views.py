from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Usuario, Mascotas , Ciudad
from .forms import UsuarioForm
from .forms import MascotasForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from . import forms
from django.http import HttpResponse



# Create your views here.
def home(request):
    mascotas = Mascotas.objects.all().order_by()
    return render(request, 'blog/Main.html', {'mascotas':mascotas })

    
    
def base(request):
    form = UsuarioForm()
    return render(request,'blog/base.html')


@login_required(login_url="/accounts/login/")
def registro(request):
    form = UsuarioForm()
    return render(request, 'blog/Registro.html', {'form': form})

@login_required(login_url="/accounts/login/")
def registro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.fecha_publicacion = timezone.now()
            usuario.author = request.user
            usuario.save()
            return redirect('blog:home')
    else:
        form = UsuarioForm()
    return render(request, 'blog/Registro.html', {'form': form})

def load_ciudades(request):
    region_id = request.GET.get('region')
    ciudades = Ciudad.objects.filter(region_id=region_id).order_by('nombre')
    return render(request, 'blog/ciudad_dropdown_list_options.html', {'ciudades': ciudades})

@login_required(login_url="/accounts/login/")
def mascota_list(request):
    user = request.user
    mascotas = Mascotas.objects.filter().order_by('fecha_publicacion')
    if user.has_perm('blog.admin'):
        return render(request, 'blog/Mascota_list.html', {'mascotas':mascotas})
    else:
        return render(request,'blog/Main.html')

@login_required(login_url="/accounts/login/")
def mascota_detail(request, pk):
    mascotas = get_object_or_404(Mascotas, pk=pk)
    return render(request, 'blog/mascota_detail.html', {'mascotas': mascotas})

@login_required(login_url="/accounts/login/")
def mascota_new(request):
    form = MascotasForm()
    return render(request, 'blog/mascota_edit.html', {'form': form})

@login_required(login_url="/accounts/login/")
def mascota_new(request):
    if request.method == "POST":
        form = MascotasForm(request.POST,request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.nombre = mascota.nombre
            mascota.fecha_publicacion = timezone.now()
            
            mascota.save()
            return redirect('blog:mascota_detail', pk=mascota.pk)
    else:
        form = MascotasForm()
    return render(request, 'blog/mascota_edit.html', {'form': form})

@login_required(login_url="/accounts/login/")
def mascota_edit(request, pk):
    mascota = get_object_or_404(Mascotas, pk=pk)
    if request.method == "POST":
        form = MascotasForm(request.POST,request.FILES, instance=mascota)
        if form.is_valid():
            mascota = form.save(commit=False)

            mascota.save()
            return redirect('blog:mascota_detail', pk=mascota.pk)
    else:
        form = MascotasForm(instance=mascota)
    return render(request, 'blog/mascota_edit.html', {'form': form})

@login_required(login_url="/accounts/login/")
def mascota_delete(request, pk):
    instance = get_object_or_404(Mascotas,pk=pk)
    instance.delete()
    return redirect('blog:mascota_list')













from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm
from django.db.models import Q



def inicio(request):
    return render(request, 'paginas/inicio.html')
    
def paciente(request):
    query = request.GET.get('q')
    if query:
        paciente = Paciente.objects.filter(
            Q(id__icontains=query) | Q(nombre__icontains=query)
        )
    else:
        paciente = Paciente.objects.all()
    return render(request, 'datos/index.html', {'paciente': paciente})

def crear(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('paciente')
    else:
        form = PacienteForm()
    return render(request, 'datos/crear.html', {'formulario': form})

def editar(request,ID):
    edi = get_object_or_404(Paciente, pk=ID)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=edi)
        if form.is_valid():
            form.save()
            return redirect('paciente')
    else:
        form = PacienteForm(instance=edi)
    return render(request, 'datos/editar.html', {'formulario': form})

def eliminar(request, ID):
    paciente = Paciente.objects.get(ID=ID)
    paciente.delete()
    return redirect('paciente')


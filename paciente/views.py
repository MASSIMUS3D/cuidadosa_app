from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from .forms import PacienteForm

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/listar.html', {'pacientes': pacientes})

def criar_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')
    return render(request, 'paciente/form.html', {'form': form})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')
    return render(request, 'paciente/form.html', {'form': form})

def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'paciente/confirma_exclusao.html', {'paciente': paciente})

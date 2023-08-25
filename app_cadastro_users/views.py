from django.shortcuts import render, redirect
from .models import Usuario
import os

def cadastrar(request): 
    cadastrar = {'title':'Cadastro'}
    return render(request, 'usuarios/cadastrar.html', cadastrar)

def listagem(request):
    usuarios = {'usuarios': Usuario.objects.all(), 'title': 'Listagem'}
    return render(request, 'usuarios/listagem.html', usuarios)

def deletar(request, id):
    usuario = Usuario.objects.get(id=id)
    
    caminho_img = usuario.arq.path
    if os.path.exists(caminho_img):
        os.remove(caminho_img)
        usuario.delete()
        return redirect('listagem')    
    else:
        usuario.delete()
        return redirect('listagem')
        
def salvar(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.arq = request.FILES.get('arq')
    novo_usuario.save()
    return redirect('listagem')

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'usuarios/editar.html', {'usuario': usuario, 'title': 'Editar'})
    
def atualizar(request, id):
    novo_nome = request.POST.get('nome')
    nova_idade = request.POST.get('idade')
    novo_cpf = request.POST.get('cpf')
    novo_arq = request.FILES.get('arq')
    usuario = Usuario.objects.get(id=id)
    
    caminho_img = usuario.arq.path
    if os.path.exists(caminho_img):
        os.remove(caminho_img)
        usuario.nome = novo_nome
        usuario.idade = nova_idade
        usuario.cpf = novo_cpf
        usuario.arq = novo_arq
        usuario.save()
        return redirect('listagem')    
    else:
        usuario.nome = novo_nome
        usuario.idade = nova_idade
        usuario.cpf = novo_cpf
        usuario.arq = novo_arq
        usuario.save()
        return redirect('listagem')
    
    
    


    
    
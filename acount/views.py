from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        print(request.user)
        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                # try:
                #     avatar = (Avatar.objects.filter(user=request.user.id))
                #     n_img = len(avatar)-1
                #     avatar_url = avatar[n_img].imagen.url
                # except:
                #     avatar_url = "../media/avatares/avatar_anonimo.png"
                return render(request, 'web_ppal/home.html', {"mensaje":f"Bienvenido {usuario}"}) #"url":avatar_url}
            else:
                return render(request, "acount/loginIncorrecto.html", {"form": form, "mensaje":"Usario o contraseña incorrecto"})

        else:
            return render(request, "acount/loginIncorrecto.html", {"form": form, "mensaje":"Usario o contraseña incorrecto"})

    form = AuthenticationForm()

    return render(request, "acount/login.html", {"form": form})

def register(request):
      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,'web_ppal/home.html' ,  {"mensaje":"Usuario Creado Exitosamente:)"})

      else:
            # form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"acount/registro.html" ,  {"form":form})

@login_required
def editarPerfil(request):
    user = request.user
    try:
        perfil = Profile.objects.get(usuario_id = request.user)
    except:
        perfil =""
    
    if request.method == 'POST':
        if "editDatos" in request.POST:  
            miFormulario = UserEditForm(request.POST)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                user.email = informacion['email']
                user.set_password(informacion['password1'])
                user.save()
            return redirect ('/') 
        
        elif "editProfile" in request.POST:
            miFormulario = ProfileCreationForm(request.POST)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                if perfil == "":
                    profile =  Profile(usuario = user, nombre = informacion['nombre'], apellido = informacion['apellido'], descripcion = informacion['descripcion'], web = informacion['web'])
                    profile.save()
                elif perfil !=0:
                    profile = Profile.objects.filter(usuario_id = request.user)
                    profile.update(usuario = user, nombre = informacion['nombre'], apellido = informacion['apellido'], descripcion = informacion['descripcion'], web = informacion['web'])
            return redirect ('../../accounts/profile/edit')         
        else:
            pass
    else:
        formDatos = UserEditForm(initial={'email': user.email})
        if perfil != "":
            formProfile = ProfileCreationForm(initial={'nombre':perfil.nombre ,'apellido':perfil.apellido,'descripcion':perfil.descripcion,'web':perfil.web})
        else:
            formProfile =  ProfileCreationForm()
    return render(request, "acount/editarPerfil.html", {"formDatos": formDatos,"formProfile":formProfile ,"usuario": user})


@login_required
def editarAvatar(request):
    if request.method == 'POST':
        form = FormAvatar(request.POST, request.FILES)
        if form.is_valid():
            # u = User.objects.get(username = request.user)
            avatar = Avatar(user = request.user, imagen = form.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'web_ppal/home.html')
    else:
        form = FormAvatar()
    return render(request, 'acount/agregarAvatar.html',{'form':form})

@login_required
def verPerfil(request):
    try:
        profile = Profile.objects.get(usuario = request.user.id)
        formProfile = ProfileDisplayForm(instance=profile)
    except:
        formProfile = ProfileDisplayForm()
    formUser = UserViewForm(instance=request.user)

    return render(request, 'acount/verPerfil.html',{"formUser":formUser, "formProfile":formProfile})






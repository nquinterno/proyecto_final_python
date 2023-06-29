from .models import *
from acount.models import * 
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# importaciones para vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from PIL import Image
import os
from django.conf import settings
import uuid


def inicio(request):
    return render(request,'web_ppal/home.html')

def aboutMe(request):
    return render(request,'web_ppal/aboutMe.html')

class PostList(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'web_ppal/post_list.html'

class PostDetalle(DetailView, LoginRequiredMixin):
    model = Post
    template_name = 'web_ppal/post_detalle.html'

class PostCreacion(CreateView, LoginRequiredMixin):
    model = Post
    success_url = '../pages'
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.autor_id = self.request.user
        imagen = form.cleaned_data['imagen']
        if imagen:
            nombre_imagen = str(uuid.uuid4()) + '.' + imagen.name.split('.')[-1]

            img = Image.open(imagen)
            img = img.resize((1080, 1080))
            image_path = os.path.join(settings.MEDIA_ROOT, 'posteos', nombre_imagen)
            img.save(image_path)
            form.instance.imagen = os.path.join('posteos', nombre_imagen)
        return super().form_valid(form)

class PostModificar(UpdateView, LoginRequiredMixin):
    model = Post
    success_url = '../pages'
    form_class = PostForm

class PostBorrar(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = '../pages/'

#Vistas para comentarios
class CommentCreacion(CreateView, LoginRequiredMixin):
    model = Comment
    success_url = '../pages/'
    form_class = CommentForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.request.GET.get('post_id')
        return super().form_valid(form)

class CommentModificar(UpdateView, LoginRequiredMixin):
    model = Comment
    success_url = '../pages/'
    form_class = CommentForm

class CommentBorrar(DeleteView, LoginRequiredMixin):
    model = Comment
    success_url = '../pages/'

#Vistas para Chats
class ChatCreacion(CreateView, LoginRequiredMixin):
    model = Chat
    success_url = '../chat'
    form_class = ChatForm
    
    def form_valid(self, form):
        form.instance.usuario1 = self.request.user
        return super().form_valid(form)

class ChatList(ListView, LoginRequiredMixin):
    model = Chat
    template_name = 'web_ppal/chat.html'

class ChatDetalle(DetailView, LoginRequiredMixin):
    model = Chat
    template_name = 'web_ppal/chat_detalle.html'

class SendMessage(CreateView, LoginRequiredMixin):
    model = Mensaje
    form_class = MessageForm
    success_url = '../'

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        form.instance.chat_id = self.request.GET.get('chat_id')
        return super().form_valid(form)
    
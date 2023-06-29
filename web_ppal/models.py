from django.db import models
from acount.models import *
from django.utils import timezone
    
class Post(models.Model):
    autor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=100, default="")
    texto = models.CharField(max_length=2500)
    imagen = models.ImageField(upload_to='posteos', null=True, blank = True,)
    fecha = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f"{self.autor_id} - {self.titulo}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500)
    fecha = models.DateTimeField(default=timezone.now)

class Chat(models.Model):
    usuario1 = models.ForeignKey(User,related_name='chats1' ,on_delete=models.CASCADE)
    usuario2 = models.ForeignKey(User,related_name='chats2',verbose_name='Destinatario',on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Chat de {self.usuario1} - {self.usuario2}"

class Mensaje(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='mensajes')
    emisor = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField(max_length=500)
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"mensaje de {self.emisor} - {self.mensaje}"




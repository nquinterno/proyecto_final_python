from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user.username}"

class Profile(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=40, default="-")
    apellido = models.CharField(max_length=40, default="-")
    descripcion = models.CharField(max_length=250, default="-")
    web = models.URLField(default="-")
    
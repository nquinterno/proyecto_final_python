from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','subtitulo' ,'texto', 'imagen']

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            if not imagen.name.endswith('.png'):
                raise forms.ValidationError("La imagen debe tener el formato PNG.")
        return imagen

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comentario']

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['usuario2']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 3}),
        }

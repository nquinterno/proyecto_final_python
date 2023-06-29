app_name = 'web_ppal'
from django.urls import path
import web_ppal.views


urlpatterns = [
    path("",web_ppal.views.inicio, name="Inicio"),
    path("about/",web_ppal.views.aboutMe,name="AboutMe"),
    path("chat",web_ppal.views.ChatList.as_view(),name="Chat"),
    path("pages/",web_ppal.views.PostList.as_view(),name="List"),
    path(r'pages/(?P<pk>)',web_ppal.views.PostDetalle.as_view(),name="Detail"),
    path(r'^nuevo$',web_ppal.views.PostCreacion.as_view(),name="New"),
    path(r'^editar/(?P<pk>\d+)$',web_ppal.views.PostModificar.as_view(),name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$',web_ppal.views.PostBorrar.as_view(),name="Delete"),
    path(r'^nuevoComentario/$',web_ppal.views.CommentCreacion.as_view(),name="NewComment"),
    path(r'^borrarComentario/(?P<pk>\d+)$',web_ppal.views.CommentBorrar.as_view(),name="DeleteComment"),
    path(r'^editarComentario/(?P<pk>\d+)$',web_ppal.views.CommentModificar.as_view(),name="EditComment"),
    path(r'^nuevoChat/$',web_ppal.views.ChatCreacion.as_view(),name="NewChat"),
    path(r'chat^(?P<pk>\d+)$',web_ppal.views.ChatDetalle.as_view(),name="DetailChat"),
    path(r'^EnviarMensaje/$', web_ppal.views.SendMessage.as_view(), name='send_message'),
]
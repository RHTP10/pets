
from django.contrib import admin
from django.urls import path
from gato.views import *
from cachorro.views import *
from core.views import *

urlpatterns = [
    path('home1/cachorro/', home1),

    path('home/gato/', home),

    path('deletar/cachorro/<int:id>', deletar_cachorro),

    path('atualizar/cachorro/<int:id>', atualizar_cachorro),

    path('cachorro/<int:id>', detalhes_cachorro),
    
    path('lista/cachorro/', lista_cachorros),

    path('deletar/gato/<int:id>', deletar_gato),

    path('atualizar/gato/<int:id>', atualizar_gato),

    path('gato/<int:id>', detalhes_gato),

    path('lista/gato/', lista_gatos),

    path('cadastro/gato/', cadastros),

    path('',core),

    path('admin/', admin.site.urls),

    path('cadastro/cachorro/', cadastros2),
    
]

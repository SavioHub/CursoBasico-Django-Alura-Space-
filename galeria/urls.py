from django.urls import path, include
from galeria.views import index
#importação do index dentro do app galeria no arquivo viwes.py
urlpatterns = [
    path('', index, name='index'),
    # path('imagem/', imagem, name='imagem'),
]
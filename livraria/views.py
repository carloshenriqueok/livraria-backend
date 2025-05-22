from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from livraria.models import Categoria, Editora, Autor, Livro
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer, LivroListSerializer  

class CategoriaView(ModelViewSet):
     queryset = Categoria.objects.all()
     serializer_class = CategoriaSerializer
     
class EditoraView(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    
class AutorView(ModelViewSet):
     queryset = Autor.objects.all()
     serializer_class = AutorSerializer
     
class LivroView(ModelViewSet):
     queryset = Livro.objects.all()

     def get_serializer_class(self):
          if self.action == "list":
               return LivroListSerializer
          elif self.action == "retrieve":
               return LivroDetailSerializer
          return LivroSerializer
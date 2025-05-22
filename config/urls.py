from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaView, EditoraView, AutorView, LivroView

router = DefaultRouter()
router.register(r"categorias", CategoriaView)
router.register(r"editoras", EditoraView)
router.register(r"autores", AutorView)
router.register(r"livros", LivroView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]

from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # A raiz redireciona para 'IndexView' (importado) como se fosse uma view 'as_view()', e nomeamos a mesma.
]
from django.contrib import admin
from django.urls import path, include  # Inclua 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Rota para incluir URLs do app 'myapp'
]
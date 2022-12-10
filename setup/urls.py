
from django.contrib import admin
from django.urls import path,include
#importação do include também
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
]

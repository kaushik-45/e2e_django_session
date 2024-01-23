
from django.urls import path
from django.urls import path,include


from . import views

app_name  = 'connect'
urlpatterns = [
    path('',views.base_index,name='base_index'),
]


from django.urls import path

from . import views

app_name = 'schools'
urlpatterns = [
     path('',views.create,name='create'),
    path('create/', views.import_csv, name='import_csv'),
    path('dict/',views.makeDictionary,name='makeDictionary'),
    path('cat/',views.schholCategory,name = 'schholCategory'),
    path('lang/',views.lamguageDist,name = 'lamguageDist'),
]

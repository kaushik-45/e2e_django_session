from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    path('',views.create,name='create'),
    path('create/', views.import_csv, name='import_csv'),
    path('dict/',views.makeDictionary,name='makeDictionary'),
    path('won/',views.matchesWon,name='matchesWon')
   
]

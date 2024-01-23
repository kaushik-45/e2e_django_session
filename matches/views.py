from django.shortcuts import render
from django.http import HttpResponse
from .models import MatchModel
from django.http import JsonResponse
from django.db.models import Count
import csv
import json
from django.core.serializers import serialize



def create(request):
    return render(request,'matches/createData.html')         


def import_csv(request):
    str="Data Alredy Exist"
    if request.method=='POST' and 'import_csv' in request.POST:    
        if not MatchModel.objects.exists(): 
            file_path = r'/Users/kaushiknandan/Desktop/python/kaushik/matches - matches.csv'
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    MatchModel.objects.create(
                        year=row['season'],
                        winner = row['winner']
                    )
            str="Data Created"        
            return render(request,'matches/first.html',{'str':str})   
        else:
            return render(request,'matches/first.html',{'str':str})     
    
           

def makeDictionary(request):
    if request.method == 'POST' and 'make_dictionary' in request.POST:    
        matches_per_season = MatchModel.objects.values('year').annotate(matches_played=Count('id')).order_by('year')
        match_list=list(matches_per_season)  
        context  = {"matches":match_list}        
        return render(request,'matches/display.html',context)



def matchesWon(request):
    if request.method == 'POST' and 'matches_won' in request.POST:    
        matches_won = MatchModel.objects.values('year','winner').annotate(matches_won = Count('id'))
        matches_won_list = list(matches_won)
        context = {"matches":matches_won_list}
        return render(request,'matches/matches_won.html',context)
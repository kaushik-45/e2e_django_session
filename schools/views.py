from django.shortcuts import render
from .models import School
from django.http import HttpResponse
import csv
from django.db.models import Count



def create(request):
    return render(request,'schools/import_data.html')         


def import_csv(request):
    if request.method=='POST' and 'import_dataVal' in request.POST:    
        str='Data Alredy Present'
        if not School.objects.exists():    
            file_path = r'/Users/kaushiknandan/Desktop/python/kaushik/primaryschool - primaryschool.csv'
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    School.objects.create(
                    name = row['name'],
                    district = row['district_name'],
                    category = row['cat'],
                    language = row['moi']

                    )
            str = "Data Created"         
            return render(request,'schools/first.html',{'str':str})  
        else:
            return render(request,'schools/first.html',{'str':str}) 

def makeDictionary(request):
    if request.method=='POST' and 'make_dictionary' in request.POST:        
        school_per_district = School.objects.values('district').annotate(count_of_schools=Count('id'))
        school_per_district_list = list(school_per_district)
        context  = {"schools":school_per_district_list}        
        return render(request,'schools/display.html',context)

def schholCategory(request):
    if request.method=='POST' and 'category' in request.POST:        
        schoolcat = School.objects.values('district','category').annotate(count_of_school = Count('id'))
        schoolcatlist = list(schoolcat)
        print(schoolcatlist)
        context = {"schools":schoolcatlist}
        return render(request,'schools/category.html',context)


def lamguageDist(request):
    if request.method=='POST' and 'lanng' in request.POST:        
        schoolcat = School.objects.values('district','language') .annotate(count_of_lang = Count('id'))
        schoolcatlist = list(schoolcat)
        print(schoolcatlist)
        context = {"schools":schoolcatlist}
        return render(request,'schools/lang.html',context)
from django.shortcuts import render
from .models import *
from django.db.models import Avg
# Create your views here.
def home(request):
    context = {}
    stu = markslist.objects.all()
    for i in stu:
        total = i.tel + i.hin
        print(total)
    context['mar'] = stu
    return render(request,"home.html", context)
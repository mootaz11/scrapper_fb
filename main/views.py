from django.shortcuts import render
from django.http import HttpResponse
from facebook_scraper import get_posts
import pandas as pd

# Create your views here.

def predict_view(request):
    posts=get_posts(request.POST.get("page"), pages=int(request.POST.get("num")))
    p=pd.DataFrame(posts)
    p.to_csv(str(request.POST.get("page"))+".csv",index=False)
    return HttpResponse("Done")
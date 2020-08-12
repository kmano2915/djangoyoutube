from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
# Create your views here

def index(request):
   return render(request,'index.html',{})

def dnload(request):
   url=request.POST.get('url', '')
   yt=YouTube(url).title
   s=YouTube(url).streams.first().download("downloader/static/video")
   yttitle='static/video/'+yt+'.mp4'
   return render(request,'dn.html',{'yttitle':yttitle})

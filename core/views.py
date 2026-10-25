from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Media, News, Event

def home(request):
    news_list = News.objects.all().order_by('-id')[:3]
    
    # timezone.now().date() sekarang sudah otomatis berpatokan pada GMT+7 (Asia/Jakarta)
    today = timezone.now().date()
    latest_events = Event.objects.filter(date__gte=today).order_by('date')[:3]
    media_list = Media.objects.all().order_by('-id')[:6]
    context = {
        'news_list': news_list,
        'events_list': latest_events,
        'media_list': media_list,
    }
    return render(request, 'home.html', context)
def media(request):
    media_list = Media.objects.all().order_by('-id')
    return render(request, 'media.html', {'media_list': media_list})
def media_detail(request, pk):
    media = get_object_or_404(Media, pk=pk)
    return render(request, 'media_detail.html', {'media': media})

def news(request):
    news_list = News.objects.all().order_by('-id')
    return render(request, 'news.html', {'news_list': news_list})

#test media
def base_test(request):
    return render(request, 'base.html')
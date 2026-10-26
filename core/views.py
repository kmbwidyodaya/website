from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Media, News, Event, Banner

def home(request):
    news_list = News.objects.all().order_by('-id')[:3]
    active_banner = Banner.objects.filter(is_active=True).order_by('-updated_at')
    # timezone.now().date() sekarang sudah otomatis berpatokan pada GMT+7 (Asia/Jakarta)
    today = timezone.now().date()
    latest_events = Event.objects.filter(date__gte=today).order_by('date')[:3]
    media_list = Media.objects.all().order_by('-id')[:6]
    context = {
        'banners': active_banner,
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

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def news(request):
    news_list = News.objects.all().order_by('-id')
    return render(request, 'news.html', {'news_list': news_list})
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': news})

#test media
def base_test(request):
    return render(request, 'base.html')
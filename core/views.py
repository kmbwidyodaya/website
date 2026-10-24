from django.shortcuts import render
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
from django.shortcuts import render
from .models import News, Event

def home(request):
    # Mengambil 2 berita terbaru dan 1 event terbaru
    latest_news = News.objects.all().order_by('-created_at')[:2]
    latest_event = Event.objects.filter(is_open_for_public=True).last()
    
    context = {
        'news_list': latest_news,
        'event': latest_event,
    }
    return render(request, 'home.html', context)
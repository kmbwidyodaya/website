from django.shortcuts import render
from django.utils import timezone
from .models import News, Event

def home(request):
    news_list = News.objects.all().order_by('-created_at')[:3]
    
    # timezone.now().date() sekarang sudah otomatis berpatokan pada GMT+7 (Asia/Jakarta)
    today = timezone.now().date()
    latest_event = Event.objects.filter(date__gte=today).order_by('date').first()
    
    context = {
        'news_list': news_list,
        'event': latest_event,
    }
    return render(request, 'home.html', context)
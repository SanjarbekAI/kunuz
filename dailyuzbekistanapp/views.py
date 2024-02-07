from django.shortcuts import render,redirect
from .models import News
from django.shortcuts import get_object_or_404
from .forms import ContactForm,CommentForm
from django.views.generic import CreateView
import requests


def ContactView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'contact_success.html')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

# Create your views here.
def NewsView(request):
    yangiliklar_slider = News.objects.all().order_by('-upload_time')[:3]
    yangiliklar_yonidagi = News.objects.all().order_by('-upload_time')[3:7]
    yangiliklar_tavsiya = News.objects.all().order_by('-upload_time')[7:13]
    
    shahar = request.GET.get('weather')

    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":f"{shahar}","days":"2"}

    headers = {
        "X-RapidAPI-Key": "f4152adb40mshddc3034080b186bp18b494jsn1bd9726ff216",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    
    bugungi_ob_havo = response.json()['current']['temp_c']
    bugungi_ob_havo_sana = response.json()['location']['localtime']
    bugungi_ob_havo_rasm = response.json()['current']['condition']['icon']
    
    context = {
        'news': yangiliklar_slider,
        'news2': yangiliklar_yonidagi,
        'news3': yangiliklar_tavsiya,
        'havo': bugungi_ob_havo,
        'sana': bugungi_ob_havo_sana,
        'rasm': bugungi_ob_havo_rasm
    }
    return render(request, 'index.html',context)

def NewsDetailView(request,slug):
    yangiliklar_slider = News.objects.all().order_by('-upload_time')[:3]
    news_detail = get_object_or_404(News,slug=slug,status=News.Status.yuklash)
    comments = news_detail.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.news = news_detail
            new_comment.user = request.user
            new_comment.save()
    else:
        form = CommentForm()  
                  
    context = {
        'news': yangiliklar_slider,
        'news_detail': news_detail,
        'form': form,
        'new_comment': new_comment,
        'comments': comments
        
    }
    
    return render(request, 'single.html', context)

def CategoryView(request):
    return render(request, 'category.html')

class NewsCreateView(CreateView):
    model = News
    template_name = 'create.html'
    fields = ('name','text','slug','category','status','image')
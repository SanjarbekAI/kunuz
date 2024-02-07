from django.urls import path
from .views import NewsView,NewsDetailView,CategoryView,ContactView,NewsCreateView

urlpatterns = [
    path("", NewsView, name='news'),
    path("yangilik/<str:slug>/",NewsDetailView,name='news_detail'),
    path('category/',CategoryView, name='category'),
    path('contact/', ContactView, name='contact'),
    path('news/add/',NewsCreateView.as_view(), name='news_add'),
]
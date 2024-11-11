from django.shortcuts import render
from .models import contents

def index(request):
    news_list = contents.objects.order_by('-create_date')
    context = {'news_list': news_list}
    return render(request, 'news/news_list.html ')
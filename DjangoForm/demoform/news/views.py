from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.
def index(request):
    return HttpResponse("Hello")

# def add_post(request):
#     a = PostForm()
#     return render(request, 'news/add_news.html', {'f':a})


# class Post(View):
#     def get(self, request):
#         a = PostForm()
#         return render(request, 'news/add_new.html')


class Save(View):
    
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f':a})

    def post(self, request):
        q = PostForm(request.POST)
        if q.is_valid():
            q.save()
            return HttpResponse('Success!!')
        else:
            return HttpResponse('not validate!!')

# def save_news(request):
#     if request.method == 'POST':
#         q = PostForm(request.POST)
#         if q.is_valid():
#             q.save()
#             return HttpResponse('Luu thanh cong!')
#         else:
#             return HttpResponse('Khong duoc validate')
#     else:
#         return HttpResponse("Khong phai post request")
    
def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f':b})

def process(request):
    if request.method == 'POST':
        q = SendEmail(request.POST)
        if q.is_valid():
            title = q.cleaned_data['title']
            email = q.cleaned_data['email']
            content = q.cleaned_data['content']
            cc = q.cleaned_data['cc']
            context = {'td':title, 'c':cc, 'ct':content, 'e':email}
            context2 = {'email_data':q}
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse("form not validate")
    else:
        return HttpResponse('Khong phai POST method')

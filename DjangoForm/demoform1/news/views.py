from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.

# def index(request):
#     return HttpResponse('Xin chào các bạn!!')
class IndexClass(View):
    def get(self, request):
        ketqua = '123456789'
        return HttpResponse(ketqua)

# class PostClass(View):
#     def get(self, request):
#         a = PostForm()
#         return render(request, 'news/add_news.html', {'f':a})

class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f': a})

    def post(self, request):
        q = PostForm(request.POST)
        if q.is_valid:
            q.save()
            return HttpResponse('Lưu thành công!!')
        else:
            return HttpResponse('Không được validate!')
    
    def put(self):
        pass

    
def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f':b})

def process(request):
    if request.method == 'POST':
        q = SendEmail(request.POST)
        if q.is_valid:
            return render(request, 'news/print_email.html', {'f':q})
        else:
            return HttpResponse('Không được validation')
    else:
        return HttpResponse('Không phải post request')
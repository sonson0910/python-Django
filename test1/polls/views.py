from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request):
    myname = "Nguyễn Sơn"
    taisan = {"Điện thoại", "Máy tính", "Máy bay"}
    context = {'name':myname, 'taisan':taisan}
    # return HttpResponse("Hello các bạn!!")
    return render(request, 'polls/index.html', context)

def viewlist(request):
    q = Question.objects.all()
    context = {'dsquest':q}
    return render(request, 'polls/question_list.html', context)

def detailView(request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, 'polls/detail_Question.html', {'qs':q})

def vote(request, question_id):
    q = Question.objects.get(pk = question_id)
    try:
        dulieu = request.POST['choice']
        c = q.choice_set.get(pk = dulieu)
    except:
        return HttpResponse("Không có câu hỏi!!")
    c.vote += 1
    c.save()
    return render(request, 'polls/result.html', {'q':q})

def ham1(request):
    return HttpResponse("<h1>Trang linh tinh</h1><p>Hello</p>")
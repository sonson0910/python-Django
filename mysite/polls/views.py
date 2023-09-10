from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    myname = "Nguyễn Sơn"
    taisan = {"Điện thoại", "Máy tính", "Máy bay", "Nhiều tiền"}
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"dsquest":list_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, "polls/detail_Question.html", {"qs": q})

def vote(request, question_id):
    q = Question.objects.get(pk = question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk = dulieu)
    except:
        HttpResponse("lỗi không có choice")
    c.vote += 1
    c.save()
    return render(request, 'polls/result.html', {'q':q})

def ham1(request):
    return HttpResponse("<h1>Hàm linh tinh</h1><p>Xin chào</p>")

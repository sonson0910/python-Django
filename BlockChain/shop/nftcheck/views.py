from django.shortcuts import render
from django.http import HttpResponse
from nftcheck.forms import PostForm
from django.views import View
from django.contrib import messages
from nft.models import Nft


# Create your views here.

def index(request):
    return HttpResponse('Hello')

class Save(View):

    def get(self, request):
        a = PostForm()
        return render(request, 'homepage/index.html', {'f':a})

    
    def post(self, request):
        q = PostForm(request.POST)
        if q.is_valid():
            q.save()
            # return HttpResponse('Success!!')
            # return render(request, 'homepage/index.html', messages=' Success')
            messages.success(request, 'Success!')
            return render(request, 'homepage/index.html', {'f':q})

        else:
            messages.warning(request, 'Not validates')
            return render(request, 'homepage/index.html', {'f': q})
            # return HttpResponse(request, 'homepage/index.html', messages='Not validates')

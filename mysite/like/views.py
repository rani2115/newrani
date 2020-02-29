from django.shortcuts import render,HttpResponse
# Create your views here.

from .models import Likes
def index(request):
    lobj = Likes.objects.get(id=1)

    return render(request,'index.html',{'likes':lobj})

def like_view(request):
    id =request.GET.get('id')
    # Likes.objects.create(like=int(id))

    lobj =Likes.objects.get(id=1)
    tlikes =lobj.like
    id=int(id)+1

    Likes.objects.filter(id=1).update(like=id)
    print('d')

    # id =int(id)+1
    return HttpResponse(tlikes)


def showLikes(request):
    lobj = Likes.objects.get(id=1)
    tlikes = lobj.like

    return HttpResponse(tlikes)
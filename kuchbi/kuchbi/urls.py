
from django.contrib import admin
from django.urls import path
from django.shortcuts import render,redirect

from django import forms





class MyForm(forms.Form):
    username =forms.CharField(max_length=12)
    password =forms.CharField(max_length=100)

from post.models import MyTable
def form_views(request):
    form =MyForm(request.POST or None)
    if form.is_valid():
        un=request.POST.get('username')
        pw=request.POST.get('password')

        # m=MyTable()
        # m.uname=un
        # m.pwd=pw
        # m.save()
        #-----
        # m=MyTable(uname=un,pwd=pw)
        # m.save()
        #------
        MyTable.objects.create(uname=un,pwd=pw)

        print('data store ho gya')
        # pp =form.cleaned_data.get('password')
        print(un,pw)
        return redirect('home')
    m =MyTable.objects.all()
    data={
        'x':form,
        'm':m
    }
    return render(request,'index.html',data)

def dash_views(request):

    data={

    }
    return render(request,'dash.html',data)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',form_views, name='home'),
    path('dash/',dash_views, name='dah'),
]


from django.shortcuts import render,HttpResponse

def meraFact(ui):
    fact=1
    for vv in range(1,ui+1):
        fact =fact *vv
    return fact


def indexpage(request):
    data=dict()
    listtable=[]
    if request.method=='POST':
        name =request.POST.get('myname')
        # data['name']=meraFact(int(name))
        getdata =int(name)
        for bb in range(1,10+1):
            vv =getdata*bb
            listtable.append(vv)

        data['table']=listtable
        data['key']=name

    return render(request,'myfile.html',data)

def service_page(request):
    return HttpResponse('Hello Data')

def service_page1(request):
    return HttpResponse('I am service wala page ')


def home(request):
    return render(request,'home.html')
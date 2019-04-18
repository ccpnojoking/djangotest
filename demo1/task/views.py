from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,RoleInfo
from django.template import loader

def home(request):
    hometem = loader.get_template("task/home.html")
    cont = {"username":"王祖贤"}
    result = hometem.render(cont)
    return HttpResponse(result)

def list(request):
    bl = BookInfo.objects.all()
    cont = {"booklist":bl}
    return render(request,"task/list.html",cont)

def detail(request,id):
    try:
        book = BookInfo.objects.get(pk = int(id))
        return render(request, "task/detail.html",{"book":book})
    except:
        return HttpResponse("输入有误")

def delete(request,id):
    try:
        BookInfo.objects.get(pk = id).delete()
        bl = BookInfo.objects.all()
        return HttpResponseRedirect("/task/list/",{"booklist":bl})
    except:
        return HttpResponse("输入有误")

def addrole(request,bookid):
    return render(request,"task/addrole.html",{"bookid":bookid})

def addrolehand(request):
    rname = request.POST["rname"]
    rgender = request.POST["rgender"]
    rcontent = request.POST["rcontent"]
    rbook = request.POST["bookid"]
    b = BookInfo.objects.get(pk = rbook)
    r = RoleInfo()
    r.rname = rname
    if rgender == "0":
        r.rgender = False
    else:
        r.rgender = True
    r.rcontent = rcontent
    r.rbook = b
    r.save()
    return HttpResponseRedirect("/task/detail/%s/"%(rbook),{"book":b})


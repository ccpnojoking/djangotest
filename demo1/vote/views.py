from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Questions,Answers

def home(request):
    h = {"username":"梅艳芳"}
    return render(request,"vote/home.html",h)

def qlist(request):
    ql = Questions.objects.all()
    return render(request,"vote/qlist.html",{"questionlist":ql})

def choice(request,id):
    q = Questions.objects.get(pk = id)
    al = q.answers_set.all()
    return render(request,"vote/choice.html",{"answerlist":al,"question":q.qcontent})

def counts(request,id):
    qu = Questions.objects.get(pk = id)
    anl = qu.answers_set.all()
    qc = qu.qcontent
    return render(request, "vote/counts.html", {"answerlist": anl, "question": qc})

def count(request):
    an = request.POST["ch"]
    an = Answers.objects.get(pk = an)
    an.acount += 1
    an.save()
    qu = an.aquestion
    anl = qu.answers_set.all()
    qc = qu.qcontent
    # return HttpResponseRedirect("/vote/home/")
    # counttem = loader.get_template("vote/count.html")
    # result = counttem.render({"answerlist":anl,"question":qc})
    # return HttpResponse(result)
    # return render(request,"vote/count.html")
    # return render(request,"vote/counts.html",{"answerlist":anl,"question":qc})
    return HttpResponseRedirect("/vote/counts/%s/"%(qu.id),{"answerlist":anl,"question":qc})



# def counts(request):
#     qu = Questions.objects.all()

    # an = []
    # for i in qu:
    #     ans = i.answers_set.all()
    #     an.append(ans)
    # return render(request,"vote/count.html",{"questionlist":qu})
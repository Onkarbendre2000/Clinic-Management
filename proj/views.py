import django.shortcuts as ds
from django.contrib.auth import login, authenticate,logout
from proj.models import info,patient,prescription
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def index(request):
    if(request.method=='POST'):
        user = request.POST.get('username')
        passw = request.POST.get('password')
        t = authenticate(username=user,password=passw)
        print(t)
        if t is not None:
            login(request,t)
            return ds.HttpResponseRedirect('homepage')
    return ds.render(request,"index.html")
def register(request):
    if(request.method=='POST'):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        age = request.POST.get('age')
        mob = request.POST.get('mob')
        reg = request.POST.get('reg')
        t = User.objects.filter(username = username)
        if not t:
            y = User.objects.create_user(username=username,password=password)
            y.save()
            login(request, y)
            c = info(email = email,name=name,age=age,mobile=mob,reg=reg)
            c.user = y
            c.save()
    return ds.render(request,"register.html")

def homepage(request):
    # if(request.user.username=='admin' or len(request.user.username)==0):
    #     return ds.render(request,'index.html')
    return ds.render(request,'homepage.html')
dict1={}
def search(request):
    if(request.method=='POST'):
        s = request.POST.get('view')
        if(s!='Search'):
            data = prescription.objects.filter(id=s)
            global dict1
            dict1 = {'data': data}
            return redirect('/pres/')
        else:
            s = request.POST.get('search')
            p = request.POST.get('cat')
            if p=='Date':
                t = prescription.objects.filter(date=s,username=request.user.username).order_by('date')
            elif p=='ID':
                t = prescription.objects.filter(id=s,username=request.user.username).order_by('date')
            elif p=='Patid':
                t = prescription.objects.filter(pid=s, username=request.user.username).order_by('date')
            else:
                t = prescription.objects.filter(dis__contains=s,username=request.user.username).order_by('date')
            print(type(prescription.pid))
            d = {'list':t}
            return ds.render(request, 'search.html', d)
    return ds.render(request,'search.html')
patid = -1
def pres(request):
    global dict1
    return ds.render(request,'pres.html',dict1)
def addpre(request):
    global patid
    t = patient.objects.filter(userrname=request.user.username)
   # print(patid)
    if(patid!=-1):
        t = patient.objects.filter(userrname=request.user.username, id=patid)
        patid = -1
    d = {'list': t}
    if(request.method=="POST"):
        id = request.POST.get('patient')
        t = patient.objects.filter(id=id)
        for i in t:
            l = i
            name = i.name
            mob = i.mobile
        username = request.user.username
        date = request.POST.get('date')
        dis = request.POST.get('dis')
        med = request.POST.get('med')
        c = prescription(name=name,mobile=mob,date=date,dis=dis,username=username,med=med)
        c.pid = l;
        c.save()
    return ds.render(request,'addpre.html',d)
def add(request):
    global patid
    patid = -1
    if (request.method == "POST"):
        name = request.POST.get('name')
        mob = request.POST.get('mob')
        user = request.user.username
        age  = request.POST.get('age')
        city = request.POST.get('city')
        c = patient(name=name,mobile=mob,userrname=user,age=age,city=city)
        c.save()
        patid = c.id
        response = redirect('/addpre/')
        return response
    return ds.render(request,'add.html')
dict = {}
def view(request):
    t = patient.objects.filter(userrname=request.user.username)
    d = {'list':t}
    if(request.method=='POST'):
        s = request.POST.get('view')
        print(s)
        if(s!='Search'):
            data = patient.objects.filter(id=s)
            global dict
            dict = {'data':data}
            return redirect('/prof/')
        else:
            sear = request.POST.get('search')
            p = request.POST.get('cat')
            if p == 'Name':
                t = patient.objects.filter(name=sear, userrname=request.user.username)
            elif p == 'ID':
                t = patient.objects.filter(id=sear, userrname=request.user.username)
            d = {'list': t}
            return ds.render(request, 'view.html', d)
    return ds.render(request,'view.html',d)
def prof(request):
    global patid
    patid = -1
    if(request.method=='POST'):
        for i in dict['data']:
            p = i
        patid = p.id
        response = redirect('/addpre')
        return response
    return ds.render(request,'prof.html',dict)
def userprofile(request):
    data = info.objects.filter(user=request.user.id)
    d = {'data':data}
    return ds.render(request,'userprofile.html',d)
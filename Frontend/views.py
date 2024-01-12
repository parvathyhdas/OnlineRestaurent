from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ItemDB
from Frontend.models import RegisterDB, ReservationDB, ContactDB
from django.contrib import messages

# Create your views here.
def homePage(reg):
    data = CategoryDB.objects.all()
    return  render(reg,"home.html",{'data':data})

def ItemPage(reg):
    item = ItemDB.objects.all()
    return render(reg,"item.html",{'item':item})

def itemFiltered(reg,iname):
    data = ItemDB.objects.filter(ItemCategory=iname)
    return render(reg,"itemFiltered.html",{'data':data})

def single_iem(reg):
    return render(reg,"single_iem.html")

def reservation(request):
    return render(request,"reservation.html")

def loginPage(request):
    return render(request,"login.html")

def saveSignup(request):
    if request.method == "POST":
        na = request.POST.get("name")
        mo = request.POST.get("mobile")
        em = request.POST.get("email")
        us = request.POST.get("username")
        pa = request.POST.get("password")
        obj = RegisterDB(Name=na,Mobile=mo,Email=em,UserName=us,Password=pa)
        obj.save()
        messages.success(request, "sign up successfully")
        return redirect(loginPage)

def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pwd = request.POST.get("password")
        if RegisterDB.objects.filter(UserName=un,Password=pwd).exists():
            request.session['UserName'] =un
            request.session['Password'] =pwd
            messages.success(request, "login successfully")
            return redirect(homePage)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(loginPage)
    return redirect(loginPage)


def Userlogout(request):
    del request.session['UserName']
    del request.session['Password']
    messages.success(request, "logout successfully")
    return redirect(loginPage)


def saveReservation(request):
    if request.method == "POST":
        da = request.POST.get("date")
        ti = request.POST.get("time")
        pe = request.POST.get("people")
        na = request.POST.get("name")
        ph = request.POST.get("phone")
        em = request.POST.get("email")
        obj = ReservationDB(Date=da,Time=ti,People=pe,Name=na,Phone=ph,Email=em)
        obj.save()
        messages.success(request, "Reservation saved successfully")
        return redirect(reservation)

def aboutPage(request):
    return render(request,"aboutPage.html")


def contactPage(request):
    return render(request,"contact.html")

def saveContact(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        ph = request.POST.get("phone")
        me = request.POST.get("message")
        obj = ContactDB(Name=na, Email=em, Phone=ph, Message=me)
        obj.save()
        messages.success(request, "Message send successfully")
        return redirect(contactPage)

def gallery(request):
    return render(request,"gallery.html")
from django.shortcuts import render,redirect
from Backend.models import CategoryDB,ItemDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your views here.
def indexPage(request):
    return render(request,"index.html")

def categoryPage(request):
    return render(request,"addCategory.html")

def saveCategory(reg):
    if reg.method == "POST":
        na = reg.POST.get("cname")
        im = reg.FILES["image"]
        des = reg.POST.get("description")
        obj = CategoryDB(Name=na,Image=im,Description=des)
        obj.save()
        return redirect(categoryPage)

def displayCategory(reg):
    data = CategoryDB.objects.all()
    return render(reg,"displayCategory.html",{'data':data})

def editCategory(reg,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(reg,"editcategory.html",{'data':data})


def updateCategory(reg,dataid):
    if reg.method == "POST":
        na = reg.POST.get("cname")
        des = reg.POST.get("description")
        try:
            img = reg.FILES["image"]
            fs = FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        CategoryDB.objects.filter(id=dataid).update(Name=na,Description=des,Image=file)
        return redirect(displayCategory)

def deleteCategory(reg,dataid):
    data = CategoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayCategory)

def itemPage(reg):
    cat = CategoryDB.objects.all()
    return render(reg,"addItems.html",{'cat':cat})

def saveItem(reg):
    if reg.method == "POST":
        ca =reg.POST.get("category")
        na =reg.POST.get("iname")
        pr =reg.POST.get("price")
        im =reg.FILES["image"]
        des =reg.POST.get("description")
        obj = ItemDB(ItemCategory=ca,ItemName=na,ItemPrice=pr,ItemImage=im,ItemDescription=des)
        obj.save()
        return redirect(itemPage)



def displayItem(reg):
    data = ItemDB.objects.all()
    return render(reg,"displayItem.html",{'data':data})

def editItem(reg,dataid):
    data = ItemDB.objects.get(id=dataid)
    cat =CategoryDB.objects.all()
    return render(reg,"editItem.html",{'data':data,'cat':cat})

def updateItem(reg,dataid):
    if reg.method == "POST":
        ca = reg.POST.get("category")
        na = reg.POST.get("iname")
        pr = reg.POST.get("price")
        des = reg.POST.get("description")
        try:
            img = reg.FILES["image"]
            fs =FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ItemDB.objects.get(id=dataid).ItemImage
        ItemDB.objects.filter(id=dataid).update(ItemCategory=ca,ItemName=na,ItemPrice=pr,ItemImage=file,ItemDescription=des)
        return redirect(displayItem)

def deleteItem(reg,dataid):
    data = ItemDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayItem)

def admin_login(request):
    return render(request,"adminLogin.html")

def adminLoginPage(request):
    if request.method == "POST":
        na = request.POST.get("name")
        pa = request.POST.get("password")
        if User.objects.filter(username__contains=na).exists():
            user = authenticate(username=na,password=pa)
            if user is not None:
                login(request,user)
                request.session['username'] =na
                request.session['password'] = pa
                return redirect(indexPage)
            else:
                return redirect(adminLoginPage)
        else:
            return redirect(admin_login)

def adminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)
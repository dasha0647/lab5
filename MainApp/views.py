from django.shortcuts import render

from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Product, Order, Locality, Client, Backup_copy, User
from .forms import FormProduct, FormOrder, FormUser, FormClient, FormBackup_copy, FormLocality

def logout(request):
    return render(request, "registration/login.html")

def index(request):
    return render(request, "index.html")

def index_product(request):
    index_form = FormProduct
    index_data = Product.objects.all()
    return render(request, "MainApp/Template_Product.html", {"form": index_form, "data": index_data})

def index_order(request):
    index_form = FormOrder
    index_data = Order.objects.all()
    return render(request, "MainApp/Template_Order.html", {"form": index_form, "data": index_data})

def index_locality(request):
    index_form = FormLocality
    index_data = Locality.objects.all()
    return render(request, "MainApp/Template_Locality.html", {"form": index_form, "data": index_data})

def index_client(request):
    index_form = FormClient
    index_data = Client.objects.all()
    return render(request, "MainApp/Template_Client.html", {"form": index_form, "data": index_data})

def index_backup_copy(request):
    index_form = FormBackup_copy
    index_data = Backup_copy.objects.all()
    return render(request, "MainApp/Template_Backup_copy.html", {"form": index_form, "data": index_data})

def index_user(request):
    index_form = FormUser
    index_data = User.objects.all()
    return render(request, "MainApp/Template_User.html", {"form": index_form, "data": index_data})

class view_product(View):
    def add_product(request):
        if request.method == "POST":
            add_data = Product()
            add_data.number = request.POST.get("number")
            add_data.name = request.POST.get("name")
            add_data.category = request.POST.get("category")
            add_data.save()
            return HttpResponseRedirect("/home/product")

    def del_product(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Product.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/product")

    def update_product(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Product.objects.get(id=update_int)
            update_data.number = request.POST.get("number")
            update_data.name = request.POST.get("name")
            update_data.category = request.POST.get("category")
            update_data.save()
            return HttpResponseRedirect("/home/product")

class view_order(View):
    def add_order(request):
        if request.method == "POST":
            add_data = Order()
            add_data.number = request.POST.get("number")
            add_data.product_id = Product.objects.get(id=request.POST.get("product_id"))
            add_data.price = request.POST.get("price")
            add_data.quantity = request.POST.get("quantity")
            add_data.customer_data = request.POST.get("customer_data")
            add_data.locality_id = Locality.objects.get(id=request.POST.get("locality_id"))
            add_data.client_id = Client.objects.get(id=request.POST.get("client_id"))
            add_data.save()
            return HttpResponseRedirect("/home/order")

    def del_order(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Order.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/order")

    def update_order(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Order.objects.get(id=update_int)
            update_data.number = request.POST.get("number")
            update_data.product_id = Product.objects.get(id=request.POST.get("product_id"))
            update_data.price = request.POST.get("price")
            update_data.quantity = request.POST.get("quantity")
            update_data.customer_data = request.POST.get("customer_data")
            update_data.locality_id = Locality.objects.get(id=request.POST.get("locality_id"))
            update_data.client_id = Client.objects.get(id=request.POST.get("client_id"))
            update_data.save()
            return HttpResponseRedirect("/home/order")

class view_locality(View):
    def add_locality(request):
        if request.method == "POST":
            add_data = Locality()
            add_data.country = request.POST.get("country")
            add_data.name_locality = request.POST.get("name_locality")
            add_data.name_region = request.POST.get("name_region")
            add_data.save()
            return HttpResponseRedirect("/home/locality")

    def del_locality(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Locality.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/locality")

    def update_locality(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Locality.objects.get(id=update_int)
            update_data.country = request.POST.get("country")
            update_data.name_locality = request.POST.get("name_locality")
            update_data.name_region = request.POST.get("name_region")
            update_data.save()
            return HttpResponseRedirect("/home/locality")

class view_client(View):
    def add_client(request):
        if request.method == "POST":
            add_data = Client()
            add_data.number = request.POST.get("number")
            add_data.title = request.POST.get("title")
            add_data.name = request.POST.get("name")
            add_data.adress = request.POST.get("adress")
            add_data.doc_num = request.POST.get("doc_num")
            add_data.doc_seria = request.POST.get("doc_seria")
            add_data.account_details = request.POST.get("account_details")
            add_data.save()
            return HttpResponseRedirect("/home/client")

    def del_client(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Client.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/client")

    def update_client(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Client.objects.get(id=update_int)
            update_data.number = request.POST.get("number")
            update_data.title = request.POST.get("title")
            update_data.name = request.POST.get("name")
            update_data.adress = request.POST.get("adress")
            update_data.doc_num = request.POST.get("doc_num")
            update_data.doc_seria = request.POST.get("doc_seria")
            update_data.account_details = request.POST.get("account_details")
            update_data.save()
            return HttpResponseRedirect("/home/client")

class view_backup_copy(View):
    def add_backup_copy (request):
        if request.method == "POST":
            add_data = Backup_copy()
            add_data.number = request.POST.get("number")
            add_data.name = request.POST.get("name")
            add_data.save()
            return HttpResponseRedirect("/home/backup_copy")

    def del_backup_copy (request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Backup_copy.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/backup_copy")

    def update_backup_copy(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Backup_copy.objects.get(id=update_int)
            update_data.number = request.POST.get("number")
            update_data.name = request.POST.get("name")
            update_data.save()
            return HttpResponseRedirect("/home/backup_copy")

class view_user(View):
    def add_user (request):
        if request.method == "POST":
            add_data = User()
            add_data.name = request.POST.get("name")
            add_data.login = request.POST.get("login")
            add_data.password = request.POST.get("password")
            add_data.save()
            return HttpResponseRedirect("/home/user")

    def del_user (request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = User.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/user")

    def update_user(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = User.objects.get(id=update_int)
            update_data.name = request.POST.get("name")
            update_data.login = request.POST.get("login")
            update_data.password = request.POST.get("password")
            update_data.save()
            return HttpResponseRedirect("/home/user")





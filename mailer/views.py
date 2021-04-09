from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
import requests
from django.http import HttpResponse, JsonResponse
import time
from .forms import *

class IndexView(ListView):
    #OLD code. Here to compare
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100

def main(request,page):
    return render(request,'mailer/index-new.html')

def home(request):
    return redirect(main,1)

def company(request,pk):
    #returns a single company
    company = Company.objects.get(pk=pk)
    company_list_new = {}
    contact_list = {}

    for contact in company.contacts.all():
        contact_list[contact.first_name + " " + contact.last_name ] = contact.get_order_count()
    company_list_new={
    "id":company.id,
    "name":company.name,
    "order_count":company.get_order_count(),
    "order_sum":company.get_order_sum(),
    "contacts": contact_list
    }

    #instead of Using Rest Framework, I used JsonResponse.Rest Framework is not necessary.  This is the simplist way for now.
    return JsonResponse(company_list_new)

def companyAmount(request):
    #returns how many companies we have
    return JsonResponse({"companyAmount":len(Company.objects.all())})


def form(request):
    #possible usage for API
    form = CompanyForm
    form2 = ContactForm
    form3 = OrderForm
    context= {'form':form, 'form2': form2, 'form3':form3}
    return render(request,'mailer/form.html',context)

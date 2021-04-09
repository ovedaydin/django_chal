from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
import requests
from django.http import HttpResponse, JsonResponse
import time

class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100


def company(request,pk):
    company = Company.objects.get(pk=pk)
    print(len(company.contacts.all()) + 1)
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


    return JsonResponse(company_list_new)

def hundreadCompanies(request,pk):
    company = Company.objects.get(pk=pk)
    print(len(company.contacts.all()) + 1)
    company_list_new = {}
    contact_list = {}

    for contact in company.contacts.all():
        contact_list[contact.first_name + " " + contact.last_name ] = contact.get_order_count()
    company_list_new={

    "name":company.name,
    "order_count":company.get_order_count(),
    "order_sum":company.get_order_sum(),
    "contacts": contact_list
    }


    return JsonResponse(company_list_new)

def main(request,page):
    return render(request,'mailer/index-new.html')
def home(request):
    return redirect(main,1)

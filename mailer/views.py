from django.shortcuts import render
from django.views.generic import ListView
from .models import *
import requests
from django.http import HttpResponse, JsonResponse


class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100


def company(request,pk):
    company = Company.objects.get(pk=pk)

    company_list_new = {}
    contact_list = {}
    for contact in company.contacts.all():
        contact_list[contact.first_name + " " + contact.last_name ] = contact.get_order_count()
    company_list_new[company.name] ={
    "order_count":company.get_order_count(),
    "order_sum":company.get_order_sum(),
    "contacts": contact_list
    }


    context = {"company_list" : company_list_new}
    print(company_list_new)
    return JsonResponse(company_list_new)

def main(request,page):
    return render(request,'mailer/index-new.html')

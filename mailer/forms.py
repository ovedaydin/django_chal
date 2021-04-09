from django.forms import ModelForm
from .models import *
#possible to use for API
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name','bic']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['company','first_name','last_name','email']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_number','company','contact','total','order_date']

from django.shortcuts import render
from expense_tracker.models import Transactions, Envelop
from expense_tracker.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.validators import validate_email,EmailValidator
#from validate_email import validate_email
from django.core.mail import send_mail
from django.conf import settings
from pprint import pprint
from django.core.exceptions import ValidationError
import datetime
from django.db.models import Sum
from django.http import HttpResponse
import re


def ajax_request(request):
    """The main web application that displays the contents in the payrolls database
    supports the pagination and sorting feature.
    """
    keyword = 'date'
    transactions = []
    id=request.user.id
    if request.GET.get('post') == 'submit':
        transactions = Transactions.objects.filter(user_id = id).order_by(keyword)
    else:
        keyword= request.GET.get('post')
        keyword = str(keyword)
        transactions = Transactions.objects.filter(user_id = id).order_by(keyword)
        


    string = ''
    string += '<h2>transaction list </h2>'
    string +='<table><thead><tr>'
    string +='<th>Date</th>'
    string +='<th>Category</th>'
    string +='<th>Payee</th>'
    string +='<th>Amount</th>'
    string +='<th>Description</th></tr></thead>'
    string +='<tbody>'
    for transaction in transactions:
        string +='<tr><td>'+ str(transaction.date) + '</td>'
        string +='<td>'+transaction.category +'</td>'
        string +='<td>'+transaction.payee+'</td>'
        string +='<td>'+ str(transaction.amounts) +'</td>'
        string +='<td>'+transaction.description+'</td></tr>'
    
    string +='</tbody></table>'
    


    return HttpResponse(string)

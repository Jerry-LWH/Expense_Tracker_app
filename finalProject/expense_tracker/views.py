#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

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
from django.views.decorators.csrf import csrf_exempt

def schema(request):
    """Returns the rendered version of the html for the schema page."""
    return render(request,'expense_tracker/schema.html')

def index(request):
    """Returns the rendered version of the html for the home/index page."""
    return render(request,'expense_tracker/index.html')

@login_required
def special(request):
    """Displays to the user once he or she is logged in."""
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    """Logs the user out and take him or her to the home/index page."""
    logout(request)
    return render(request, 'expense_tracker/index.html', {})


def username_retrieve(request):
    """Allows the user to retrieve his or her username."""
    if request.method == 'GET':
        method = True
        return render(request,'expense_tracker/username_retrieve.html',{'method':method})
    elif request.method == 'POST':
        method = False
        email = request.POST.get('email')
        exist = False
        try:
            user = User.objects.get(email__exact = email)
            exist = True
        except User.DoesNotExist:
            exist = False
        if exist:
            username_email(user)
        return render(request,'expense_tracker/username_retrieve.html',
                      {'method':method,
                       'exist':exist})
        
def register(request):
    """Create an account with the provided information and store it in the database."""
    registered = False
    user_exist = False
    user_form=None
    profile_form = None
    check_unique1 = None
    invalid_email = False

    if request.method == 'POST':
        check_unique1 = check_unique(request)    
        #Invalid email address
        if check_unique1 == 'invalid_email':
            invalid_email = True
            pprint('good')
    #Create the account.
    if request.method == 'POST' and check_unique1 == True:
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                if 'profile_pic' in request.FILES:
                    print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
                email(request,user)
            else:
                print(user_form.errors,profile_form.errors)
    #The user already has an account.
    elif request.method == 'POST' and check_unique1 == False:
        user_exist = True
    else:
         user_form = UserForm()
         profile_form = UserProfileInfoForm()
    return render(request,'expense_tracker/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'user_exist':user_exist,
                           'invalid_email':invalid_email })


def check_unique(request):
    """Checks if there is exist an account under the email address or username."""
    pprint('inside')
    exist = None
    email = request.POST.get('email')
    username = request.POST.get('username')
    try:
        user = User.objects.get(email__exact = email)
        exist = True
    except User.DoesNotExist:
        exist = False
        try:
            user = User.objects.get(username__exact = username)
            exist = True
        except User.DoesNotExist:
            exist = False
            if check_email(request) ==False:
                pprint('invalid')
                exist = True
                return 'invalid_email'
    if exist==True:
        return False
    else:
        return True


def check_email(request):
    """Checks if the email is valid."""
    email = request.POST.get('email')
    valid = None
    try:
        validate_email(email)
        valid = True
    except ValidationError as e:
        valid = False
    
    pprint('validation')
    pprint(valid)
    return valid


def user_login(request):
    """Attempt to sign in with the provided credentials."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            #Valid - take the user to his or her account.
            if user.is_active:
                login(request,user)
                #return HttpResponseRedirect(reverse('index'))
                return render(request, 'expense_tracker/index.html', {})
            else:
                return HttpResponse("Your account was inactive.")
        #Invalid credentials
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'expense_tracker/login.html', {})


def email(request,user):
    """Sends a welcome email after the user created an account."""
    subject = 'Thank you for registering to our site!'
    message = 'Hello '+user.first_name+'! Welcome to Expense Tracker App.'
    message = message + 'Thank you for registering, it means the world to us.'
    message = message + '404PageNotFound Team'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail( subject, message, email_from, recipient_list )

def username_email(user):
    """Sends an email to the user with the his or her username."""
    subject = 'Username Retrival'
    message = 'Hello ' + user.first_name + '! Your Username is '+ user.username
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail( subject, message, email_from, recipient_list )

def user_settings(request):
    """Displays the information provided during registration and allow the user to edit them."""
    if request.method == 'GET':
        pprint('in get')
        return render(request,'expense_tracker/settings.html',
                      {'method':'GET'})
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = request.user
        updated = False
        invalid_username = False
        if username != '':
            try:
                user = User.objects.get(username__exact = username)
                invalid_username=True
                pprint('user exist')
            except User.DoesNotExist:
                pprint('user not exist')
                user.username = username

        if firstname != '' and invalid_username == False:
            user.first_name = firstname
        if lastname != ''and invalid_username == False:
            user.last_name = lastname
        if password != ''and invalid_username == False:
            user.set_password(password)
        
        if invalid_username == False:
            if firstname != '' or lastname!='' or username != '' or password !='':
                user.save()
                updated = True
          
                if username != '' or password != '' :  #if username updated, must relogin again
                    logout(request)
                    return render(request, 'expense_tracker/index.html', {'username_changed':True})

        return render(request,'expense_tracker/settings.html',
                      {'method':'POST',
                       'updated':updated,
                       'invalid_username':invalid_username})

@csrf_exempt
def main_page(request):
    """Calculates the funds for the summary content in the main page."""
    id = request.user.id
    #getting envelop value by category
    try:
        gas_v = Envelop.objects.get(user_id = id, category = 'gas').amounts
    except:
        gas_v =0
    try:
        grocery_v = Envelop.objects.get(user_id = id, category = 'grocery').amounts
    except:
        grocery_v = 0
    try:
        dinning_v = Envelop.objects.get(user_id = id, category = 'dinning').amounts
    except:
        dinning_v = 0
    try:
        housing_v = Envelop.objects.get(user_id = id, category = 'housing_utility').amounts
    except:
        housing_v = 0
    try:
        healthcare_v = Envelop.objects.get(user_id = id, category = 'health_care').amounts
    except:
        healthcare_v = 0
    try:
        entertainment_v = Envelop.objects.get(user_id = id, category = 'entertainment').amounts
    except:
        entertainment_v = 0
    try:
        other_v = Envelop.objects.get(user_id = id, category = 'other').amounts
    except:
        other_v = 0

    totalFund = gas_v + grocery_v + dinning_v + housing_v + healthcare_v + entertainment_v + other_v
    usedFund = 0
    availableFund=0
    gas_entries = Transactions.objects.filter(user_id= id, category = 'gas')
    gas_sum = 0
    if gas_entries:
        for i in gas_entries:
            gas_sum += i.amounts
    usedFund += gas_sum
    gas_sum = gas_v - gas_sum        
            
    grocery_entries = Transactions.objects.filter(user_id= id, category = 'grocery')
    grocery_sum = 0
    if grocery_entries:
        for i in grocery_entries:
            grocery_sum += i.amounts
    usedFund+=grocery_sum
    grocery_sum = grocery_v - grocery_sum        

    dinning_entries = Transactions.objects.filter(user_id= id, category = 'dinning')
    dinning_sum = 0
    if dinning_entries:
        for i in dinning_entries:
            dinning_sum += i.amounts
    usedFund += dinning_sum
    dinning_sum = dinning_v-dinning_sum

    housing_entries = Transactions.objects.filter(user_id= id, category = 'housing_utility')
    housing_sum = 0
    if housing_entries:
        for i in housing_entries:
            housing_sum += i.amounts
    usedFund +=housing_sum
    housing_sum = housing_v-housing_sum

    healthcare_entries = Transactions.objects.filter(user_id= id, category = 'healthcare')
    healthcare_sum = 0
    if healthcare_entries:
        for i in healthcare_entries:
            healthcare_sum += i.amounts
    usedFund += healthcare_sum
    healthcare_sum = healthcare_v - healthcare_sum
            
    entertainment_entries = Transactions.objects.filter(user_id= id, category = 'entertainment')
    entertainment_sum = 0
    if entertainment_entries:
        for i in entertainment_entries:
            entertainment_sum += i.amounts
    usedFund += entertainment_sum
    entertainment_sum = entertainment_v - entertainment_sum


    other_entries = Transactions.objects.filter(user_id= id, category = 'other')
    other_sum = 0
    if other_entries:
        for i in other_entries:
            other_sum += i.amounts
    usedFund += other_sum
    other_sum = other_v - other_sum
    availableFund = totalFund-usedFund

    if request.method == 'GET':
        method = 'GET'
        transactions=[]
        transactions = Transactions.objects.filter(user_id = id)
        #check if need to sent alert email
        alert =False
        alert_categories = []
        if gas_v != 0 and (gas_v-gas_sum)/gas_v > 0.9 or gas_v == 0 and gas_sum < 0:
            alert=True
            alert_categories.append('Gas')
        if grocery_v !=0 and (grocery_v-grocery_sum)/grocery_v > 0.9 or grocery_v ==0 and grocery_sum <0:
            alert=True
            alert_categories.append('Grocery')
        if dinning_v !=0 and (dinning_v-dinning_sum)/dinning_v > 0.9 or dinning_v ==0 and dinning_sum < 0:
            alert=True
            alert_categories.append('Dinning')
        if housing_v !=0 and (housing_v-housing_sum)/housing_v > 0.9 or housing_v==0 and housing_sum < 0:
            alert=True
            alert_categories.append('Housing/Utility')
        if healthcare_v !=0 and (healthcare_v-healthcare_sum)/healthcare_v > 0.9 or healthcare_v ==0 and healthcare_sum < 0:
            alert=True
            alert_categories.append('Healthcare')
        if entertainment_v !=0 and (entertainment_v-entertainment_sum)/entertainment_v > 0.9 or entertainment_v ==0 and entertainment_sum <0:
            alert=True
            alert_categories.append('Entertainment')
        if other_v != 0 and (other_v-other_sum)/other_v > 0.9 or other_v ==0 and other_sum < 0:
            alert=True
            alert_categories.append('Other')

        return render(request, 'expense_tracker/main.html', 
                      {'transactions':transactions, 'method':method,'alert':alert,'alert_categories':alert_categories,
                       'totalFund':totalFund, 'availableFund':availableFund, 'gas_v':gas_v, 'grocery_v': grocery_v, 'dinning_v': dinning_v,
                       'housing_v':housing_v,'healthcare_v':healthcare_v, 'entertainment_v':entertainment_v, 'other_v':other_v,
                       'gas_sum':gas_sum, 'grocery_sum': grocery_sum, 'dinning_sum': dinning_sum,
                      'housing_sum':housing_sum,'healthcare_sum':healthcare_sum, 'entertainment_sum':entertainment_sum, 'other_sum':other_sum})

    if request.method == 'POST':
        #delete transaction
        transaction_id = request.POST.get('delete_button')
        if transaction_id != None:
            pprint('in delete')
            pprint(transaction_id)
            #remove transaction
            Transactions.objects.filter(id=transaction_id).delete()
            #fetch rows
            method="POST"
            id = request.user.id
            transactions=[]
            transactions = Transactions.objects.filter(user_id = id)
            
            #update the values for envelop in summary content
            try:
                gas_v = Envelop.objects.get(user_id = id, category = 'gas').amounts
            except:
                gas_v =0
            try:
                grocery_v = Envelop.objects.get(user_id = id, category = 'grocery').amounts
            except:
                grocery_v = 0
            try:
                dinning_v = Envelop.objects.get(user_id = id, category = 'dinning').amounts
            except:
                dinning_v = 0
            try:
                housing_v = Envelop.objects.get(user_id = id, category = 'housing_utility').amounts
            except:
                housing_v = 0
            try:
                healthcare_v = Envelop.objects.get(user_id = id, category = 'health_care').amounts
            except:
                healthcare_v = 0
            try:
                entertainment_v = Envelop.objects.get(user_id = id, category = 'entertainment').amounts
            except:
                entertainment_v = 0
            try:
                other_v = Envelop.objects.get(user_id = id, category = 'other').amounts
            except:
                other_v = 0

            totalFund = gas_v + grocery_v + dinning_v + housing_v + healthcare_v + entertainment_v + other_v
            usedFund = 0
            availableFund=0
        
            totalFund = gas_v + grocery_v + dinning_v + housing_v + healthcare_v + entertainment_v + other_v
            usedFund = 0
            availableFund=0

            gas_entries = Transactions.objects.filter(user_id= id, category = 'gas')
            gas_sum = 0
            if gas_entries:
                for i in gas_entries:
                    gas_sum += i.amounts
            usedFund += gas_sum
            gas_sum = gas_v - gas_sum

            grocery_entries = Transactions.objects.filter(user_id= id, category = 'grocery')
            grocery_sum = 0
            if grocery_entries:
                for i in grocery_entries:
                    grocery_sum += i.amounts
            usedFund+=grocery_sum
            grocery_sum = grocery_v - grocery_sum
        
            dinning_entries = Transactions.objects.filter(user_id= id, category = 'dinning')
            dinning_sum = 0
            if dinning_entries:
                for i in dinning_entries:
                    dinning_sum += i.amounts
            usedFund += dinning_sum
            dinning_sum = dinning_v-dinning_sum

            housing_entries = Transactions.objects.filter(user_id= id, category = 'housing_utility')
            housing_sum = 0
            if housing_entries:
                for i in housing_entries:
                    housing_sum += i.amounts
            usedFund +=housing_sum
            housing_sum = housing_v-housing_sum

            healthcare_entries = Transactions.objects.filter(user_id= id, category = 'healthcare')
            healthcare_sum = 0
            if healthcare_entries:
                for i in healthcare_entries:
                    healthcare_sum += i.amounts
            usedFund += healthcare_sum
            healthcare_sum = healthcare_v - healthcare_sum

            entertainment_entries = Transactions.objects.filter(user_id= id, category = 'entertainment')
            entertainment_sum = 0
            if entertainment_entries:
                for i in entertainment_entries:
                    entertainment_sum += i.amounts
            usedFund += entertainment_sum
            entertainment_sum = entertainment_v - entertainment_sum
        
        
            other_entries = Transactions.objects.filter(user_id= id, category = 'other')
            other_sum = 0
            if other_entries:
                for i in other_entries:
                    other_sum += i.amounts
            usedFund += other_sum
            other_sum = other_v - other_sum
            availableFund = totalFund-usedFund
            
            #check if need to sent alert email
            alert =False
            alert_categories = []
            if gas_v != 0 and (gas_v-gas_sum)/gas_v > 0.9 or gas_v == 0 and gas_sum < 0:
                alert=True
                alert_categories.append('Gas')
            if grocery_v !=0 and (grocery_v-grocery_sum)/grocery_v > 0.9 or grocery_v ==0 and grocery_sum <0:
                alert=True
                alert_categories.append('Grocery')
            if dinning_v !=0 and (dinning_v-dinning_sum)/dinning_v > 0.9 or dinning_v ==0 and dinning_sum < 0:
                alert=True
                alert_categories.append('Dinning')
            if housing_v !=0 and (housing_v-housing_sum)/housing_v > 0.9 or housing_v==0 and housing_sum < 0:
                alert=True
                alert_categories.append('Housing/Utility')
            if healthcare_v !=0 and (healthcare_v-healthcare_sum)/healthcare_v > 0.9 or healthcare_v ==0 and healthcare_sum < 0:
                alert=True
                alert_categories.append('Healthcare')
            if entertainment_v !=0 and (entertainment_v-entertainment_sum)/entertainment_v > 0.9 or entertainment_v ==0 and entertainment_sum <0:
                alert=True
                alert_categories.append('Entertainment')
            if other_v != 0 and (other_v-other_sum)/other_v > 0.9 or other_v ==0 and other_sum < 0:
                alert=True
                alert_categories.append('Other')


            return render(request, 'expense_tracker/main.html',
                          {'transactions':transactions,'method':method,'alert':alert,'alert_categories':alert_categories,
                           'totalFund':totalFund,'availableFund':availableFund, 'gas_v':gas_v, 'grocery_v': grocery_v, 'dinning_v': dinning_v,
                           'housing_v':housing_v,'healthcare_v':healthcare_v, 'entertainment_v':entertainment_v, 'other_v':other_v,
                           'gas_sum':gas_sum, 'grocery_sum': grocery_sum, 'dinning_sum': dinning_sum,
                           'housing_sum':housing_sum,'healthcare_sum':healthcare_sum, 'entertainment_sum':entertainment_sum, 'other_sum':other_sum})
        #add transactions
        else:
            method='POST'
            amount = request.POST.get('amount')
            payee = request.POST.get('payee')
            description = request.POST.get('description')
            category = request.POST.get('category')
            date = request.POST.get('date')
            #convert date format
            date = datetime.datetime.strptime(date,"%m/%d/%Y").strftime("%Y-%m-%d")
        
            #verify amount input
            valid_amount= True
            try:
                amount = int(amount)
                if amount <= 0:
                    valid_amount = False
            except:
                valid_amount = False

            #allow insert
            if valid_amount == True:
                transaction = Transactions()
                user = request.user
                transaction.date = date
                transaction.user = user
                transaction.amounts = amount
                transaction.payee = payee
                transaction.description = description
                transaction.category = category
                transaction.save()
                
            #fetch rows
            id = request.user.id
            transactions=[]
            transactions = Transactions.objects.filter(user_id = id)
            try:
                gas_v = Envelop.objects.get(user_id = id, category = 'gas').amounts
            except:
                gas_v =0
            try:
                grocery_v = Envelop.objects.get(user_id = id, category = 'grocery').amounts
            except:
                grocery_v = 0
            try:
                dinning_v = Envelop.objects.get(user_id = id, category = 'dinning').amounts
            except:
                dinning_v = 0
            try:
                housing_v = Envelop.objects.get(user_id = id, category = 'housing_utility').amounts
            except:
                housing_v = 0
            try:
                healthcare_v = Envelop.objects.get(user_id = id, category = 'health_care').amounts
            except:
                healthcare_v = 0
            try:
                entertainment_v = Envelop.objects.get(user_id = id, category = 'entertainment').amounts
            except:
                entertainment_v = 0
            try:
                other_v = Envelop.objects.get(user_id = id, category = 'other').amounts
            except:
                other_v = 0

            totalFund = gas_v + grocery_v + dinning_v + housing_v + healthcare_v + entertainment_v + other_v
            usedFund = 0
            availableFund=0
        
            totalFund = gas_v + grocery_v + dinning_v + housing_v + healthcare_v + entertainment_v + other_v
            usedFund = 0
            availableFund=0

            gas_entries = Transactions.objects.filter(user_id= id, category = 'gas')
            gas_sum = 0
            if gas_entries:
                for i in gas_entries:
                    gas_sum += i.amounts
            usedFund += gas_sum
            gas_sum = gas_v - gas_sum

            grocery_entries = Transactions.objects.filter(user_id= id, category = 'grocery')
            grocery_sum = 0
            if grocery_entries:
                for i in grocery_entries:
                    grocery_sum += i.amounts
            usedFund+=grocery_sum
            grocery_sum = grocery_v - grocery_sum
        
            dinning_entries = Transactions.objects.filter(user_id= id, category = 'dinning')
            dinning_sum = 0
            if dinning_entries:
                for i in dinning_entries:
                    dinning_sum += i.amounts
            usedFund += dinning_sum
            dinning_sum = dinning_v-dinning_sum

            housing_entries = Transactions.objects.filter(user_id= id, category = 'housing_utility')
            housing_sum = 0
            if housing_entries:
                for i in housing_entries:
                    housing_sum += i.amounts
            usedFund +=housing_sum
            housing_sum = housing_v-housing_sum

            healthcare_entries = Transactions.objects.filter(user_id= id, category = 'healthcare')
            healthcare_sum = 0
            if healthcare_entries:
                for i in healthcare_entries:
                    healthcare_sum += i.amounts
            usedFund += healthcare_sum
            healthcare_sum = healthcare_v - healthcare_sum

            entertainment_entries = Transactions.objects.filter(user_id= id, category = 'entertainment')
            entertainment_sum = 0
            if entertainment_entries:
                for i in entertainment_entries:
                    entertainment_sum += i.amounts
            usedFund += entertainment_sum
            entertainment_sum = entertainment_v - entertainment_sum
                
            other_entries = Transactions.objects.filter(user_id= id, category = 'other')
            other_sum = 0
            if other_entries:
                for i in other_entries:
                    other_sum += i.amounts
            usedFund += other_sum
            other_sum = other_v - other_sum
            availableFund = totalFund-usedFund
            #check if need to sent alart email
            alert =False
            alert_categories = []
            if gas_v != 0 and (gas_v-gas_sum)/gas_v > 0.9 or gas_v == 0 and gas_sum < 0:
                alert=True
                alert_categories.append('Gas')
            if grocery_v !=0 and (grocery_v-grocery_sum)/grocery_v > 0.9 or grocery_v ==0 and grocery_sum <0:
                alert=True
                alert_categories.append('Grocery')
            if dinning_v !=0 and (dinning_v-dinning_sum)/dinning_v > 0.9 or dinning_v ==0 and dinning_sum < 0:
                alert=True
                alert_categories.append('Dinning')
            if housing_v !=0 and (housing_v-housing_sum)/housing_v > 0.9 or housing_v==0 and housing_sum < 0:
                alert=True
                alert_categories.append('Housing/Utility')
            if healthcare_v !=0 and (healthcare_v-healthcare_sum)/healthcare_v > 0.9 or healthcare_v ==0 and healthcare_sum < 0:
                alert=True
                alert_categories.append('Healthcare')
            if entertainment_v !=0 and (entertainment_v-entertainment_sum)/entertainment_v > 0.9 or entertainment_v ==0 and entertainment_sum <0:
                alert=True
                alert_categories.append('Entertainment')
            if other_v != 0 and (other_v-other_sum)/other_v > 0.9 or other_v ==0 and other_sum < 0:
                alert=True
                alert_categories.append('Other')

            return render(request, 'expense_tracker/main.html',
                          {'transactions':transactions,'valid_amount':valid_amount,'method':method,'alert':alert,'alert_categories':alert_categories,
                           'totalFund':totalFund, 'availableFund':availableFund, 'gas_v':gas_v, 'grocery_v': grocery_v, 'dinning_v': dinning_v,
                           'housing_v':housing_v,'healthcare_v':healthcare_v, 'entertainment_v':entertainment_v, 'other_v':other_v,
                           'gas_sum':gas_sum, 'grocery_sum': grocery_sum, 'dinning_sum': dinning_sum,
                           'housing_sum':housing_sum,'healthcare_sum':healthcare_sum, 'entertainment_sum':entertainment_sum, 'other_sum':other_sum})



def getEnvelopValue(request):
    """Add all of the evelops to an array."""
    id = request.user.id
    #values for envelop
    try:
        gas_v = Envelop.objects.get(user_id = id, category = 'gas').amounts
    except:
        gas_v =0
    try:
        grocery_v = Envelop.objects.get(user_id = id, category = 'grocery').amounts
    except:
        grocery_v = 0
    try:
        dinning_v = Envelop.objects.get(user_id = id, category = 'dinning').amounts
    except:
        dinning_v = 0
    try:
        housing_v = Envelop.objects.get(user_id = id, category = 'housing_utility').amounts
    except:
        housing_v = 0
    try:
        healthcare_v = Envelop.objects.get(user_id = id, category = 'health_care').amounts
    except:
        healthcare_v = 0
    try:
        entertainment_v = Envelop.objects.get(user_id = id, category = 'entertainment').amounts
    except:
        entertainment_v = 0
    try:
        other_v = Envelop.objects.get(user_id = id, category = 'other').amounts
    except:
        other_v = 0

    values = []
    values.append(gas_v)
    values.append(grocery_v)
    values.append(dinning_v)
    values.append(housing_v)
    values.append(healthcare_v)
    values.append(entertainment_v)
    values.append(other_v)
    return values


#envelop view
def envelop(request):
    """Create evelops (categories for different types of expenses)."""
    #get envelop values
    values = getEnvelopValue(request)

    #iterateble object for days in envelop.html
    list = []
    for i in range(4,31):
        list.append(i)

    if request.method == 'GET':
        return render(request, 'expense_tracker/envelop.html',
                      {'values':values,'days':list})
    
    #editing the envelop
    if request.method == 'POST':
        id = request.user.id
        start_date = request.POST.get('start_date')
        user = request.user
        gas = request.POST.get('gas')
        grocery = request.POST.get('grocery')
        dinning = request.POST.get('dinning')
        housing_utility = request.POST.get('housing_utility')
        healthcare = request.POST.get('health_care')
        entertainment = request.POST.get('entertainment')
        other = request.POST.get('other')
        #first time adding
        exist = False
        try:
            gas_row = Envelop.objects.get(user_id = id, category = 'gas')
        except:
            gas_row =False
        try:
            grocery_row = Envelop.objects.get(user_id = id, category = 'grocery')
        except:
            grocery_row = False
        try:
            dinning_row = Envelop.objects.get(user_id = id, category = 'dinning')
        except:
            dinning_row = False
        try:
            housing_row = Envelop.objects.get(user_id = id, category = 'housing_utility')
        except:
            housing_row = False
        try:
            healthcare_row = Envelop.objects.get(user_id = id, category = 'health_care')
        except:
            healthcare_row = False
        try:
            entertainment_row = Envelop.objects.get(user_id = id, category = 'entertainment')
        except:
            entertainment_row = False
        try:
            other_row = Envelop.objects.get(user_id = id, category = 'other')
        except:
            other_row = False
            
        #check if all input valid
        allow_modify = True
        try:
            gas = int(gas)
            grocery = int(grocery)
            dinning = int(dinning)
            housing_utility = int(housing_utility)
            healthcare = int(healthcare)
            entertainment = int(entertainment)
            other = int(other)
            if gas < 0 or grocery < 0 or dinning < 0 or housing_utility < 0 or healthcare < 0 or entertainment < 0 or other < 0:
                allow_modify = False
        except:
            allow_modify = False
                
        #modifying envelop
        if allow_modify == True:
            if gas != '' and  gas_row == False:
                envelop = Envelop()
                envelop.user = user
                envelop.start_date = start_date
                envelop.category = 'gas'
                envelop.amounts = gas
                envelop.save()
            elif gas != '' and gas_row != False:
                pprint('inside change')
                gas_row.amounts = gas
                gas_row.save()

            #grocery_row = Envelop.objects.get(user_id = id, category = 'grocery')
            if grocery != '' and grocery_row == False:
                envelop = Envelop()
                envelop.user = user
                envelop.start_date = start_date
                envelop.category = 'grocery'
                envelop.amounts = grocery
                envelop.save()
            elif grocery != '' and grocery_row!= False:
                grocery_row.amounts = grocery
                grocery_row.save()

            #dinning_row = Envelop.objects.get(user_id = id, category = 'dinning')
            if dinning != '' and dinning_row == False:
                envelop = Envelop()
                envelop.user = user
                envelop.start_date = start_date
                envelop.category = 'dinning'
                envelop.amounts = dinning
                envelop.save()
            elif dinning != '' and dinning_row != False:
                dinning_row.amounts =dinning
                dinning_row.save()
            
            #housing_row = Envelop.objects.get(user_id = id, category = 'housing_utility')
            if housing_utility != '' and housing_row == False:
                envelop = Envelop()
                envelop.user = user
                envelop.start_date = start_date
                envelop.category = 'housing_utility'
                envelop.amounts = housing_utility
                envelop.save()
            elif housing_utility != '' and housing_row != False:
                housing_row.amounts =housing_utility
                housing_row.save()

            #healthcare_row = Envelop.objects.get(user_id = id, category = 'healthcare')
            if healthcare != '' and healthcare_row == False:
                envelop = Envelop()
                envelop.user = user
                envelop.start_date = start_date
                envelop.category = 'health_care'
                envelop.amounts = healthcare
                envelop.save()
            elif healthcare != '' and healthcare_row != False:
                healthcare_row.amounts =healthcare
                healthcare_row.save()

            #entertainment_row = Envelop.objects.get(user_id = id, category = 'entertainment')
            if entertainment != '' and entertainment_row == False:
                envelop = Envelop()
                envelop.user = user
                envelop.start_date = start_date
                envelop.category = 'entertainment'
                envelop.amounts = entertainment
                envelop.save()
            elif entertainment != '' and entertainment_row != False:
                entertainment_row.amounts =entertainment
                entertainment_row.save()

            #other_row = Envelop.objects.get(user_id = id, category = 'other')
            if other != '' and other_row == False:
                envelop = Envelop()
                envelop.user = user
                envelop.start_date = start_date
                envelop.category = 'other'
                envelop.amounts = other
                envelop.save()
            elif other != '' and other_row != False:
                other_row.amounts =other
                other_row.save()
                
                #get updated envelop values
        values = getEnvelopValue(request)
            
    return render(request, 'expense_tracker/envelop.html',
                  {'days':list,'values':values, 'allow_modify':allow_modify})





def reset_done(request):
    """""Returns the rendered version of the html for the password reset page."""
    return render(request, 'registration/password_reset_done.html',{})

def reset_complete(request):
    """Returns the rendered version of the html for the password reset completion page."""
    return render(request, 'registration/password_reset_complete.html',{})




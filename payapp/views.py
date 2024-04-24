from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from register.models import Userprofile
from .models import *
# Create your views here.
@login_required(login_url='/auth/login/') 
def Home(request):
    data = Userprofile.objects.get(id=request.user.id)
  
    context = {
        'data' : data,
    }
    return render(request, 'payapp/home.html',context)
@login_required(login_url='/auth/login/') 
def send_money(request):
    if request.method == 'POST':
        email = request.POST['email']
        amount =  request.POST['amount']
        currency =  request.POST['currency']
        
        conversion_rates = {
            ('GBP', 'GBP'): 1,
            ('EUR', 'EUR'): 1,
            ('USD', 'USD'): 1,
            ('GBP', 'USD'): 1.37,
            ('GBP', 'EUR'): 1.17,
            ('USD', 'GBP'): 0.73,
            ('USD', 'EUR'): 0.86,
            ('EUR', 'GBP'): 0.85,
            ('EUR', 'USD'): 1.16,
        }

        
        receiver = Userprofile.objects.get(email=email)
        sender = Userprofile.objects.get(id=request.user.id)
        
        
        receiver_currency = receiver.currency
        sender_currency = sender.currency
        rate_for_sender = conversion_rates[(currency, sender_currency)]
        sender_amount = int(amount) * rate_for_sender
        print(f"sender amount is {sender_amount},Rate for sender is {rate_for_sender}")
        
        if sender.amount >= sender_amount :
            # deductin money from sender account 
            sender.amount = sender.amount - int(sender_amount)
            sender.save()
            
            
            
            rate = conversion_rates[(currency, receiver_currency)]
            converted_amount = int(amount) * rate
            receiver.amount = receiver.amount + int(converted_amount)
            receiver.save()
            
        else:
            return HttpResponse("Not enough amount to send")
        
        # from_currency = sender.currency
        # if (from_currency, to_currency) not in conversion_rates:
        #     return JsonResponse({'error': f"Conversion rate not available for {from_currency} to {to_currency}"}, status=400)

        # rate = conversion_rates[(from_currency, to_currency)]
        # converted_amount = amount * rate
        # sender.amount = sender.amount - int(amount)
        # user.amount = user.amount + int(amount)
        # sender.save()
        # user.save()
        return redirect('/')
    data = Userprofile.objects.get(id=request.user.id)
  
    context = {
        'data' : data,
    }
    return render(request, 'payapp/sendmoney.html',context)


@login_required(login_url='/auth/login/') 
def request_money(request):
    if request.method == 'POST':
        email = request.POST['email']
        amount =  request.POST['amount']
        currency =  request.POST['currency']
        to = Userprofile.objects.get(email=email)
        From = Userprofile.objects.get(id=request.user.id)
        obj = reqeusted_money(amount=amount,currency=currency,to=to,From=From)
        obj.save()
        return HttpResponse("success")
    data = Userprofile.objects.get(id=request.user.id)
    requests = reqeusted_money.objects.filter(to=request.user.id,status='Pending')
    requests_from_others = reqeusted_money.objects.filter(From=request.user.id)
  
    context = {
        'data' : data,
        'requests' : requests,
        'requests_from_others' :requests_from_others
    }
    return render(request, 'payapp/request_money.html',context)




def convert_currency(request,from_currency,to_currency,amount):
    if request.method == 'GET':
        print("Converting currency")
        
        # from_currency = request.GET.get('from_currency')
        # to_currency = request.GET.get('to_currency')
        # amount = float(request.GET.get('amount', 0))  
        # print(f'{from_currency} to {to_currency}')
        
        conversion_rates = {
            ('GBP', 'GBP'): 1,
            ('EUR', 'EUR'): 1,
            ('USD', 'USD'): 1,
            ('GBP', 'USD'): 1.37,
            ('GBP', 'EUR'): 1.17,
            ('USD', 'GBP'): 0.73,
            ('USD', 'EUR'): 0.86,
            ('EUR', 'GBP'): 0.85,
            ('EUR', 'USD'): 1.16,
        }

        if (from_currency, to_currency) not in conversion_rates:
            return JsonResponse({'error': f"Conversion rate not available for {from_currency} to {to_currency}"}, status=400)

        rate = conversion_rates[( from_currency,to_currency)]
        converted_amount = amount * rate

        return JsonResponse({'converted_amount': converted_amount,"target_currency":to_currency,'rate':rate}, status=200)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def notifications(request):
    return render(request, 'payapp/notifications.html')
def transactions(request):
    return render(request,'payapp/transactions.html')

def permission(request,id):
    context = {'id':id}
    return render(request, 'payapp/request_permission.html',context)
def approve(request,id):
    obj = reqeusted_money.objects.get(id=id)
    currency = obj.currency
    amount = obj.amount
    conversion_rates = {
            ('GBP', 'GBP'): 1,
            ('EUR', 'EUR'): 1,
            ('USD', 'USD'): 1,
            ('GBP', 'USD'): 1.37,
            ('GBP', 'EUR'): 1.17,
            ('USD', 'GBP'): 0.73,
            ('USD', 'EUR'): 0.86,
            ('EUR', 'GBP'): 0.85,
            ('EUR', 'USD'): 1.16,
        }

        
    receiver = obj.From
    sender = obj.to
        
        
    receiver_currency = receiver.currency
    sender_currency = sender.currency
    rate_for_sender = conversion_rates[(currency, sender_currency)]
    sender_amount = int(amount) * rate_for_sender
    print(f"sender amount is {sender_amount},Rate for sender is {rate_for_sender}")
        
    if sender.amount >= sender_amount :
            # deductin money from sender account 
        sender.amount = sender.amount - int(sender_amount)
        sender.save()
            
            
            
        rate = conversion_rates[(currency, receiver_currency)]
        converted_amount = int(amount) * rate
        receiver.amount = receiver.amount + int(converted_amount)
        receiver.save()
        obj.status = 'Success'
        obj.save()
        return HttpResponse("Success")
            
    else:
        return HttpResponse("Not enough amount to send")
   



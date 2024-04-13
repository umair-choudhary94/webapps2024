from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/auth/login/') 
def Home(request):
    return render(request, 'payapp/home.html')
@login_required(login_url='/auth/login/') 
def send_money(request):
    return render(request, 'payapp/sendmoney.html')
@login_required(login_url='/auth/login/') 
def request_money(request):
    return render(request, 'payapp/request_money.html')




def convert_currency(request):
    if request.method == 'GET':
        print("Converting currency")
        
        from_currency = request.GET.get('from_currency')
        to_currency = request.GET.get('to_currency')
        amount = float(request.GET.get('amount', 0))  
        print(f'{from_currency} to {to_currency}')
        
        conversion_rates = {
            ('GBP', 'USD'): 1.37,
            ('GBP', 'EUR'): 1.17,
            ('USD', 'GBP'): 0.73,
            ('USD', 'EUR'): 0.86,
            ('EUR', 'GBP'): 0.85,
            ('EUR', 'USD'): 1.16,
        }

        if (from_currency, to_currency) not in conversion_rates:
            return JsonResponse({'error': f"Conversion rate not available for {from_currency} to {to_currency}"}, status=400)

        rate = conversion_rates[(from_currency, to_currency)]
        converted_amount = amount * rate

        return JsonResponse({'converted_amount': converted_amount}, status=200)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




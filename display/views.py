from django.shortcuts import render
from .cryptodata import CryptoData

def home(request):
    crypto_data = CryptoData()

    c_list = crypto_data.get_currencies()
    currencies = dict()
    for i in range(5):
        currencies[c_list[i]['id']] = {
            'name' : c_list[i]['name'],
            'market_cap' : c_list[i]['market_cap'],
            'total_volume' : c_list[i]['total_volume'],
            'current_price' : c_list[i]['current_price']
        }
    context = {
        #how many to show
        'range' : range(5),
        'currencies' : currencies
    }
    return render(request, 'display/index.html', context)

from django.shortcuts import render
from .cryptodata import CryptoData
from operator import *

def home(request):
    crypto_data = CryptoData()

    c_list = crypto_data.get_currencies()
    currencies = dict()
    for i in range(25):
        currencies[c_list[i]['id']] = {
            'name' : c_list[i]['name'],
            'market_cap' : c_list[i]['market_cap'],
            'total_volume' : c_list[i]['total_volume'],
            'current_price' : c_list[i]['current_price'],
            'market_cap_rank': c_list[i]['market_cap_rank']
        }

	#sort currencies by market cap rank
    currencies = dict(sorted(currencies.items(),key=lambda x:getitem(x[1],'market_cap_rank')))
    context = {
        'currencies' : currencies
    }
    return render(request, 'display/index.html', context)

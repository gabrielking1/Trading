from django.shortcuts import render,redirect,get_object_or_404
from .models import Trader, Entry
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    
        search  = request.GET.get('search')
        
        
        if search:
            trader =  Trader.objects.filter(name__iexact = search)
            for trade in trader:
                
                # return redirect(dashboard, name = search)
                return HttpResponseRedirect(reverse("dashboard",args={trade.id}))
            else:
                messages.error(request, f'{search} not found')
                return render(request, 'index.html')
        return render(request, 'index.html')
   

def dashboard(request, id):
    # trader = get_object_or_404(Trader, name=name)
    trader = Trader.objects.get(id=id )
    
    entries = Entry.objects.filter(trader=trader).values('timestamp', 'profit_loss')
    profit =entries.filter(profit_loss__gt=0).aggregate(Sum('profit_loss'))['profit_loss__sum']
    loss = entries.filter(profit_loss__lte=0).aggregate(Sum('profit_loss'))['profit_loss__sum']
    user_data = []
    user_data.append({
            'id': trader.id,
            'username': trader.name,
            'profitLossData': list(entries),
        })
    
    gain = trader.capital - 100.00
    
    deficit = 100.00 - trader.capital
    return render(request, 'admin1.html', {'trader': trader, 'entries': entries,'user_data': user_data,'profit':profit,'loss':loss,
    'deficit':deficit,'gain':gain})

def admin(request):
    traders = Trader.objects.all()
    data = []
    
    for trader in traders:
        trader_data = {}
        trader_data['name'] = trader.name
        trader_data['capital'] = trader.capital
        trader_data['total_profit'] = Entry.objects.filter(trader=trader,profit_loss__gt=0).aggregate(Sum('profit_loss'))['profit_loss__sum']
        trader_data['total_loss'] = Entry.objects.filter(trader=trader, profit_loss__lte=0).aggregate(Sum('profit_loss'))['profit_loss__sum']
        data.append(trader_data)
    
    
    return render(request, 'admin.html', {'traders': data})

def check(request):
    search  = request.GET.get('search')
    trader =  Trader.objects.filter(name = search).exists()
    
    if trader:
        return HttpResponse('<div style="color:green"> trader exists </div>')
    else:
        return HttpResponse('<div style="color:red"> trader not found </div>')
     

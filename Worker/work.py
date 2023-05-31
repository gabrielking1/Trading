from Myapp.models import Trader, Entry
import random
from datetime import datetime

def handler():
    traders = Trader.objects.all()
    entries = Entry()
    gettime  = datetime.now().strftime("%H:%M:%S")

    for trader in traders:
        profit_loss = random.uniform(-10, 10)
       

        Entry.objects.filter(trader=trader).update_or_create(trader=trader, profit_loss=profit_loss)
        # # Entry.objects.create(
        trader.capital += profit_loss
        print(f"this is trader {trader.name} and capital is {trader.capital} and {profit_loss} {gettime}")
        trader.save()

       
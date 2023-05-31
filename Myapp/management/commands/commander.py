import random
from django.core.management.base import BaseCommand
from Myapp.models import Trader
from faker import Faker

class Command(BaseCommand):
    help = 'Simulates profit and loss for traders'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10):
            trader_name = fake.name()
            trader = Trader.objects.create(name=trader_name, capital=100.0)
           
            trader.save()
            self.stdout.write(self.style.SUCCESS(f"Trader created with {trader.pk} - {trader.name}"))

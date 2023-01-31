from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from shopapp.models import Order



class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="Admin")
        order = Order.objects.get_or_create(
            delivery_address="Lenina st., 18",
            promocode="SALE12345",
            user=user,
        )
        self.stdout.write(f"Create order {order}")

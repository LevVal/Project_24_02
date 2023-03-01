# from django.db import models
# from django.contrib.auth.models import User
# from keyring.backends import null
#
#
# class Product(models.Model):
#     class Meta:
#         ordering = ["name", "price"]
#
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField(null=False, blank=True)
#     discount = models.SmallIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     archived = models.BooleanField(default=False)
#
# class Order(models.Model):
#     delivery_address = models.TextField(null=True, blank=True)
#     promocode = models.CharField(max_length=20, null=False, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     products = models.ManyToManyField(Product, related_name="orders")
#
# # Create your models here.

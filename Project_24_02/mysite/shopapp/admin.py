from django.contrib import admin
from .models import Product, Order
from django.http import HttpRequest
from django.db.models import QuerySet
from .admin_mixins import ExportAsCSVMixin

class OrderInline(admin.TabularInline):
    model = Product.orders.through

#class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through

@admin.action(description='Unarchived products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet) -> None:
    queryset.update(archived=False)

@admin.action(description='Archived products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet) -> None:
    queryset.update(archived=True)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [OrderInline,]
    list_display = ('pk', 'name', 'description_short', 'price', 'discount', 'archived')
    list_display_links = ('pk', 'name')
    ordering = 'pk', #'-name
    search_fields = 'name', 'description'
    fieldsets = [
        (None, {'fields': ['name', 'description',]}),
        ("Price options", {'fields': ['price', 'discount'],
                           "classes": ['wide', 'collapse']}),
        ("Extra options", {'fields': ['archived'],
                           "classes": ['wide', 'collapse'],
                           "description": "Extra options. This product has been archived. Field 'archived' is for soft delete."}),
        ]
    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 40:
           return obj.description
        return obj.description[:40] + '...'


#admin.site.register(Product, ProductAdmin)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]
    list_display = "delivery_address", "promocode", "created_at", "user_verbose"

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related("products") #.all()

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
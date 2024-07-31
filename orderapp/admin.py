from django.contrib import admin
from orderapp.models import Order,OrderDetail

# Register your models here.
class ManageOrder(admin.ModelAdmin):
    list_display=["fullname","phone","address","total","created"]
    search_fields=["fullname","address"]
    list_filter=["created"]
    list_per_page=9
class ManageOder_detial(admin.ModelAdmin):
    list_display=["product","price","quantity","created"]
    search_fields=["product","price"]
    list_filter=["created"]
    list_per_page=9
admin.site.register(Order,ManageOrder)
admin.site.register(OrderDetail,ManageOder_detial)
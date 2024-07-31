from django.contrib import admin
from productapp.models import Product
# Register your models here.
class ManageProuct(admin.ModelAdmin):
    list_display=["name","price","stock","isTranding"]
    list_editable=["price","stock","isTranding"]
    list_per_page=3
    search_fields=["name"]
    list_filter=["isTranding"]
admin.site.register(Product,ManageProuct)

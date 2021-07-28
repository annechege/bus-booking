from django.contrib import admin
from .models import Transactions,AddBusModel,AddRouteModel,AdduserModel

# Register your models here.

admin.site.register(Transactions)
admin.site.register(AddBusModel)
admin.site.register(AddRouteModel)
admin.site.register(AdduserModel)
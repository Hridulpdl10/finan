from django.contrib import admin
from .models import Materials, AccountType, District, SubDistrict, AccountApplication

# Register your models here.

admin.site.register(Materials)
admin.site.register(AccountType)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(AccountApplication)

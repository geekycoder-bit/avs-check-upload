from django.contrib import admin

from .models import Contact, Images, Clients, Franchise, Employee, Products, Machines, Credentials
# Register your models here.


admin.site.register(Contact)
admin.site.register(Images)
admin.site.register(Clients)
admin.site.register(Franchise)
admin.site.register(Employee)
admin.site.register(Products)
admin.site.register(Machines)
admin.site.register(Credentials)
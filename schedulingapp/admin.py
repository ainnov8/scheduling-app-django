from django.contrib import admin

# Register your models here.
from schedulingapp.models import User, Company, Branch, Department, Employee, Client, Event

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Event)

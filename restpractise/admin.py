from django.contrib import admin
from restpractise.models import Company,Employee



class CompanyAdmin(admin.ModelAdmin ):
    list_display=('name','location','type') 
    search_fields=['name',]

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','company')
    list_filter=['company']

# Register your models here.

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
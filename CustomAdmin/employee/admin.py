from django.contrib import admin
from .models import EmployeeRecords, EmployeePreviousExperience, CheckEmployee, EmployeeRecordsProxy
from .views import check_employeeView
from django.urls import path

# Register your models here.
class EmployeePreviousExperienceAdmin(admin.TabularInline):
    model= EmployeePreviousExperience
    extra = 1
 
@admin.action(description='Active Employee',)
def make_active(modeladmin, request, queryset):
    queryset.update(status = True)

@admin.action(description='Inactive Employee',)
def make_inactive(modeladmin, request, queryset):
    queryset.update(status = False)


@admin.register(EmployeeRecords)
class EmployeeRecordsAdmin(admin.ModelAdmin):
    list_display =('employee_name','designation','employee_salary','status')
    fields=('employee_name','designation','employee_salary')
    inlines=[EmployeePreviousExperienceAdmin,]
    actions = [make_active, make_inactive]


@admin.register(CheckEmployee)
class CheckEmployeeAdmin(admin.ModelAdmin):
    
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        
        return [
            path('', check_employeeView, name=view_name),
        ]

@admin.register(EmployeeRecordsProxy)
class EmployeeRecordsProxyadmin(admin.ModelAdmin):
    fields= ('employee_id','employee_name','designation','status')
    readonly_fields=('employee_id','employee_name','designation','status')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CheckEmployeeForm
from .models import EmployeeRecords

# Create your views here.
@staff_member_required
def check_employeeView(request):

    checkemployee = CheckEmployeeForm
    if request.method == 'POST':
        fm = checkemployee(request.POST)
        if fm.is_valid():
            employee = EmployeeRecords.objects.filter(employee_id= fm.cleaned_data['Check_Employee']).first()
            if employee:
                return redirect(f'/admin/employee/employeerecordsproxy/{employee.employee_id}/change')
            else:
                messages.error(request,"Employee Id Does not exist")
                return redirect('/admin/employee/checkemployee/')

    return render(request, 'employee/check.html', {'form':checkemployee})

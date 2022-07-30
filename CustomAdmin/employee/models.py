from django.db import models

# Create your models here.
class EmployeeRecords(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name= models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    employee_salary = models.PositiveIntegerField()
 
    def __str__(self):
        return str(self.employee_id)
 
   
    class Meta:
        verbose_name='Employee Record'
        verbose_name_plural='Employee Records'
 
 
class EmployeePreviousExperience(models.Model):
    employee_id = models.ForeignKey(EmployeeRecords, on_delete=models.CASCADE)
    previous_company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date =models.DateField()
 
 
    def __str__(self):
        return self.previous_company_name
 
    class Meta:
        verbose_name='Employee Previous Experience'
        verbose_name_plural='Employee Previous Experience'

class CheckEmployee(models.Model):
    class Meta:
        verbose_name = 'Check Employee'
        verbose_name_plural = 'Check Employee'


class EmployeeRecordsProxy(EmployeeRecords):
    class Meta:
        proxy = True
        verbose_name = 'Proxy Employee Record'
        verbose_name_plural = 'Proxy Employee Records'
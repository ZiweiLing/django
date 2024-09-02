from django.db import models
from student.models import Student

# Create your models here.
class Employee(models.Model):
    POSITION_S = 'S'
    POSITION_C = 'C'
    POSITION_E = 'E'
    POSITION_A = 'A'
    POSITION_B = 'B'
    POSITION_CHOICES = [
        (POSITION_S, 'Seller'),
        (POSITION_C, 'Consultant'),
        (POSITION_E, 'Essay Writing'),
        (POSITION_A, 'Application'),
        (POSITION_B, 'SUPERVISOR'),
    ]
    CONTRACT_P = 'P'
    CONTRACT_F = 'F'
    CONTRACT_R = 'R'
    CONTRACT_CHOICES = [
        (CONTRACT_P, 'Parttime'),
        (CONTRACT_F, 'Fulltime'),
        (CONTRACT_R, 'Resigned'), 
    ]
    employeeName = models.CharField(max_length=255)
    background = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    performance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    contractStatus = models.CharField(max_length=1, choices=CONTRACT_CHOICES, default=CONTRACT_F)
    # one student should be assigned multiple teachers
    students = models.ManyToManyField(Student, related_name='teachers')

    def __str__(self):
        return self.employeeName
    
    class Meta:
        ordering = ['employeeName']
        

class CID(models.Model):
    cid = models.CharField(max_length=255)
    # set one to one relationship between cid and employee, and set employee as the primary key to avoid one to many relationship
    # if employee is deleted, cid would be deleted
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
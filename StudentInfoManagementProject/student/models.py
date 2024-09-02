from django.db import models

class Student(models.Model):
    EDUCATION_U = 'U'
    EDUCATION_G = 'G'
    EDUCATION_CHOICES = [
        (EDUCATION_U, 'Undergraduate'),
        (EDUCATION_G, 'Graduate'),
    ]

    CONTRACT_S = 'S'
    CONTRACT_F = 'F'
    CONTRACT_CHOICES = [
        (CONTRACT_S, 'Success'),
        (CONTRACT_F, 'Failed'),
    ]
    studentName = models.CharField(max_length=255)
    education = models.CharField(max_length=1, choices=EDUCATION_CHOICES, default=EDUCATION_U)
    university = models.CharField(max_length=255, null=True, blank=True)
    grades = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    contractStatus = models.CharField(max_length=1, choices=CONTRACT_CHOICES, default=CONTRACT_F)
    contractTime = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.studentName
    
    class Meta:
        ordering = ['studentName']
        db_table = 'StudentInformation'
        indexes = [
            models.Index(fields=['university', 'grades'])
        ]


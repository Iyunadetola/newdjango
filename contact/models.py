from django.db import models

# Create your models here.
class MyContact(models.Model):
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    subjectmatter=models.CharField(max_length=200, null=True)
    phonenumber=models.CharField(max_length=200, null=True)
    message=models.TextField(max_length=200, null=True)
    

    def __str__(self):
        return f'{self.name} {self.email}'




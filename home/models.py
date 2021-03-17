from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Images(models.Model):
    bg1_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    bg2_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    bg3_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    worker1_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    worker2_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    worker3_image = models.ImageField(upload_to='assests/upload', default="", blank="True")

class Clients(models.Model):
    client_id = models.AutoField
    client_name = models.CharField(max_length=50)
    client_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.client_name

class Franchise(models.Model):
    franchise_id = models.AutoField
    franchise_name = models.CharField(max_length=50)
    franchise_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.client_name

class Employee(models.Model):
    employee_id = models.AutoField
    employee_name = models.CharField(max_length=50)
    employee_designation = models.CharField(max_length=50, default="")
    employee_desc = models.CharField(max_length=1000, blank='True')
    employee_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.employee_name

class Products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000, blank='True')
    image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.product_name

class Machines(models.Model):
    Machine_id = models.AutoField
    Machine_name = models.CharField(max_length=50)
    Machine_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.Machine_name

class Credentials(models.Model):
    Credential_id = models.AutoField
    Credential_name = models.CharField(max_length=50)
    Credential_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.Credential_name


class Contact(models.Model):
    Contact_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = PhoneNumberField()
    msg = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


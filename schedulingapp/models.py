from django.db import models

# Create your models here.     
class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150, unique=True)
    date = models.DateField()
    address = models.TextField()
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=25)
    contact_person = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    company_logo = models.ImageField(max_length=200, upload_to='images/')
    description = models.CharField(max_length=255)
    website = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s %s" % (self.name, self.contact_person)
    
class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    join_date = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=150, null=True, blank=True)
    
    profile_image = models.ImageField(max_length=200, upload_to='profile_images/')  
        
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
       
    def __str__(self):
        return "%s %s" % (self.name, self.branch)
    
class Client(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=150)
    province = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=50)
    profile_image = models.ImageField(max_length=200, upload_to='profile_images/')  
    join_date = models.DateField(auto_now_add=True)
    
    employees = models.ForeignKey(Employee, on_delete=models.PROTECT)
    
    def __str__(self):
        return "%s %s" % (self.name, self.employee)
    
class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=128)
    start_time = models.DateField()
    end_time = models.DateField()
    
    note = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return "%s %s" % (self.name, self.employee)
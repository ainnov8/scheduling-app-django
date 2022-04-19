from rest_framework import serializers
from schedulingapp.models import Branch, Company, Department, Employee, Client, Event, User
from django.contrib.auth.models import Group

class CompanySerializer(serializers.ModelSerializer):
    company_logo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True, required=False)
    # users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    
    class Meta:
        model = Company
        fields = '__all__'
        
class BranchSerializer(serializers.ModelSerializer):
    # company = serializers.PrimaryKeyRelatedField(source='company.name', read_only=True) 
    
    class Meta:
        model = Branch
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    
    class Meta:
        model = Department
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    profile_image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True, required=False)
    
    class Meta:
        model = Employee
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True, required=False)
    employees = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())
    
    class Meta:
        model = Client
        fields = '__all__'
                
class UserSerializer(serializers.ModelSerializer):   
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all(), required=False)     
    # company = serializers.PrimaryKeyRelatedField(source='company.name', read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': { 'write_only': True }
        }
        
        def create(self, *args, **kwargs):
            user = super().create(*args, **kwargs)
            password = user.password
            user.set_password(password)
            user.save()
            return user
        
        def update(self, *args, **kwargs):
            user = super().update(*args, **kwargs)
            password = user.password
            user.set_password(password)
            user.save()
            return user
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'
        

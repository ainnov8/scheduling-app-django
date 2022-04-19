from django.shortcuts import render
from django.contrib.auth.models import Group
from schedulingapp.models import Company, Branch, Department, Employee, Client, Event, User
from schedulingapp.serializers import CompanySerializer, BranchSerializer, DepartmentSerializer, EmployeeSerializer, ClientSerializer, UserSerializer, EventSerializer, GroupSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from tenants.utils import tenant_from_request

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

# branch  
class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = BranchSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

# department  
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DepartmentSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

# employee   
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    
# client   
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
#     @action(detail=True, methods=[ 'POST', 'PUT' ])
#     def create(self, serializer):
#         instance = serializer.save()
#         instance.set_password(instance.password)
#         instance.is_active = True
#         instance.save()
        
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.is_active = True
        instance.save()
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
        
class CreateAdminUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.is_active = True
        instance.is_staff = True
        instance.save()
    
# groups 
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = GroupSerializer
    
# events    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EventSerializer
    
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    

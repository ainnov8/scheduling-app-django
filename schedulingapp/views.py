from django.shortcuts import render
from django.contrib.auth.models import Group, User
from schedulingapp.models import Company, Branch, Department, Employee, Client, Event
from schedulingapp.serializers import CompanySerializer, BranchSerializer, DepartmentSerializer, EmployeeSerializer, ClientSerializer, UserSerializer, EventSerializer, GroupSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    permission_classes = [ permissions.IsAuthenticated ]


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    permission_classes = [ permissions.IsAuthenticated ]
    
class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]
    
class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]
    
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]
    
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]
    
class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]
    
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    permission_classes = [ permissions.IsAuthenticated ]
    
# Create your views here.
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = CompanySerializer

#branch  
# class BranchViewSet(viewsets.ModelViewSet):
#     queryset = Branch.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = BranchSerializer

# department  
# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = DepartmentSerializer

# # employee   
# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = EmployeeSerializer
    
# # client   
# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = ClientSerializer

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
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = GroupSerializer
    
# events    
# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = EventSerializer
    

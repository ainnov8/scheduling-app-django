"""techleft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from schedulingapp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# router = routers.DefaultRouter()

# router.register('api/companies', views.CompanyViewSet, basename='company')
# router.register('api/branches', views.BranchViewSet, basename='branch')
# router.register('api/departments', views.DepartmentViewSet, basename='department')
# router.register('api/employees', views.EmployeeViewSet, basename='employee')
# router.register('api/clients', views.ClientViewSet, basename='client')
# router.register('api/groups', views.GroupViewSet, basename='group')
# router.register('api/events', views.EventViewSet, basename='event')

urlpatterns = [
    # path('', include(router.urls)),
    path('api/companies/', views.CompanyList.as_view(), name='company-list'),
    path('api/companies/', views.CompanyDetail.as_view(), name='company-detail'),
    
    path('api/branches/', views.BranchList.as_view(), name='branch-list'),
    path('api/branches/', views.BranchDetail.as_view(), name='branch-detail'),
    
    path('api/departments/', views.DepartmentList.as_view(), name='department-list'),
    path('api/departments/', views.DepartmentDetail.as_view(), name='department-detail'),
    
    path('api/employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('api/employees/', views.EmployeeDetail.as_view(), name='employee-detail'),
    
    path('api/clients/', views.ClientList.as_view(), name='client-list'),
    path('api/clients/', views.ClientDetail.as_view(), name='client-detail'),
    
    path('api/groups/', views.GroupList.as_view(), name='group-list'),
    path('api/groups/', views.GroupDetail.as_view(), name='group-detail'),
    
    path('api/events/', views.EventList.as_view(), name='event-list'),
    path('api/events/', views.EventDetail.as_view(), name='event-detail'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/users/', views.UserList.as_view(), name='users-list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('api/admin/', views.CreateAdminUser.as_view(), name='admin-user'),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns += router.urls

"""
URL configuration for retia_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin', admin.site.urls),
    path('device', devices),
    path('device/<str:hostname>', device_detail),
    path('device/<str:hostname>/interface', interfaces),
    path('device/<str:hostname>/interface/<str:name>', interface_detail),
    path('device/<str:hostname>/interface/<str:name>/in_throughput', interface_in_throughput),
    path('device/<str:hostname>/interface/<str:name>/out_throughput', interface_out_throughput),
    path('device/<str:hostname>/static-route', static_route),
    path('device/<str:hostname>/routing/ospf-process', ospf_processes),
    path('device/<str:hostname>/routing/ospf-process/<int:id>', ospf_process_detail),
    path('device/<str:hostname>/acl', acls),
    path('device/<str:hostname>/acl/<str:name>', acl_detail),
    path('detector', detectors),
    path('detector/<str:device>', detector_detail),
    path('detector/<str:device>/sync', detector_sync),
    path('detector/<str:device>/start', detector_start),
    path('monitoring/buildinfo', monitoring_buildinfo),
    path('log/activity', log_activity),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]

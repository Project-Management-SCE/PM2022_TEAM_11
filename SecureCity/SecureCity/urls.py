"""SecureCity URL Configuration

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
from django.urls import path
from HomePage import views as HomePageV
from Authentication import views as AuthenticationV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageV.home, name="homepage"),
    path(r'PatrolManagement/', HomePageV.patrol_management, name='PatrolManagement'),
    path(r'PatrolManagement/CreatePatrol', HomePageV.create_patrol, name='CreatePatrol'),
    path('AddParent/', AuthenticationV.AddParent, name="AddParent"),
    path('Login/', AuthenticationV.loginU, name="Login"),
    path('logout/', AuthenticationV.logoutuser, name="logoutuser"),
    path('adminPage/', AuthenticationV.adminP, name="adminPage"),
    path('Patrol/', HomePageV.parent_patrol, name='parent_patrol'),
    path('mypage/', AuthenticationV.residentPage, name='resident_page'),

]

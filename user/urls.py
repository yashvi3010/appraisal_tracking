from django.contrib import admin
from django.urls import path,include
from user import views
from .views import LoginView,EmployeeSignUpView,HrSignUpView

urlpatterns = [
    path('index/',views.index, name= 'index'),
    path('login/',LoginView.as_view(), name= 'login'),
    path('attend/',views.attend, name= 'attend'),
    path('forget_psw/', views.ForgetPsw, name= 'forget_psw'),
    # path('logout/',UserLogout.as_view(), name= 'logout'),
    path('employee_signup/',EmployeeSignUpView.as_view(), name= 'employee_signup'),
    path('hr_signup/',HrSignUpView.as_view(), name= 'hr_signup'),
    path('meetings/',views.meetings, name= 'meetings'),
    path('details',views.details, name= 'details'),
    

    


]
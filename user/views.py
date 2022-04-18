from django.shortcuts import render,redirect
from .forms import EmployeeSignupForm, HrSignupForm
from .models import User
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView


# Create your views here.
def index(request):
     return render(request, 'index.html')

def meetings(request):
     return render(request, 'meetings.html')

def details(request):
     return render(request, 'details.html')   

def attend(request):
     return render(request, 'attendance/attendance.html')        

# def UserLogin(request):
#      return render(request,'templates/login.html')
 
# def UserSignUp(request):
#      return render(request,'templates/signup.html')
 

# Create your views here.
"""class UserLogin(LoginView):
    template_name = 'login.html'
    
class UserSignup(CreateView):
    model = User
    fields = ['password','email', 'username']
    template_name = 'signup.html'
    success_url = 'user/'

class UserLogout(LogoutView):
     pass   """ 



# ------------------------- company ---------------------------

class EmployeeSignUpView(CreateView):
    model = User
    
    form_class = EmployeeSignupForm
    template_name = 'registrations/employee_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class HrSignUpView(CreateView):
    model = User
    form_class = HrSignupForm
    template_name = 'registrations/hr_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')        



class LoginView(LoginView):
    template_name = 'registrations/login.html'

    def get(self, request, *args, **kwargs):
        print(self.request.user)
        return self.render_to_response(self.get_context_data()) 

def ForgetPsw(request):
    return render(request, 'registrations/forget_psw.html')

    
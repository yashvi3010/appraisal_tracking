# Create your views here.
from email.mime import image
from django.forms import models
from django.shortcuts import render
from django.template import context
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Project, Project_module
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail




class AddProject(CreateView):
    model = Project
    fields = ['title', 'description', 'technology', 'estimatedHours', 'startDate', 'completionDate']
    template_name = 'project/add_project.html'
    success_url = '/appraisall_tracking/view'

class ViewProject(ListView):
    model = Project
    projects = model.objects.all()
    context_object_name = 'projects'
    template_name = 'project/view_project.html'    

class DetailProject(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/detail_project.html'

class DeleteProject(DeleteView):
    model = Project
    template_name = 'project/delete_project.html'
    success_url = '/appraisall_tracking/view'


class UpdateProject(UpdateView):
    model = Project
    fields = ['title', 'description', 'technology', 'estimatedHours', 'startDate', 'completionDate']
    template_name = 'project/update_project.html'
    success_url = '/appraisall_tracking/view'


def sendmail(request):
   subject = 'welcome'
   message = 'welcome to Appraisal tracking'
   email_from = settings.EMAIL_HOST_USER
   recipient_list = ['shahyashvi3010@gmail.com', 'kavsjobanputra@gmail.com'] 
   send_mail(subject, message, email_from, recipient_list)
   return HttpResponse("mail sent")

   
       

class AddProjectModule(CreateView):
    model = Project_module
    fields = ['project','moduleName', 'description', 'estimatedHours', 'startDate', 'completionDate']
    template_name = 'projectmodule/add_projectmodule.html'
    success_url = '/appraisall_tracking/viewmodule'

class ViewProjectModule(ListView):
    model = Project_module
    project = model.objects.all()
    context_object_name = 'projectmodules'
    template_name = 'projectmodule/view_projectmodule.html'    

class DetailProjectModule(DetailView):
    model = Project_module
    context_object_name = 'project'
    template_name = 'projectmodule/detail_projectmodule.html'

class DeleteProjectModule(DeleteView):
    model = Project_module
    template_name = 'projectmodule/delete_projectmodule.html'
    success_url = '/appraisall_tracking/viewmodule'


class UpdateProjectModule(UpdateView):
    model = Project_module
    fields = ['module_name', 'description', 'estimatedHours', 'startDate', 'completionDate']
    template_name = 'projectmodule/update_projectmodule.html'
    success_url = '/appraisall_tracking/viewmodule'    
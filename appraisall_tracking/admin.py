from django.contrib import admin
from .models import Project, Project_module, Project_team 

admin.site.register(Project)
admin.site.register(Project_team)
admin.site.register(Project_module)



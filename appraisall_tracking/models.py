from django.db import models
from django.forms import DateField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    technology = models.CharField(max_length=100)
    estimatedHours = models.IntegerField()
    startDate = models.DateField(null= True)
    completionDate = models.DateField(null= True)

    class Meta():
        db_table = 'project'

    def __str__(self):
        return self.title
    

class Project_team(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta():
        db_table = 'project_team'

    def __str__(self):
        return self.project.title
    

class Project_module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    moduleName = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    estimatedHours = models.IntegerField()
    startDate = models.DateField()
    completionDate = models.DateField()

    class Meta:
        db_table = 'project_module'

    def __str__(self):
        return self.project.title
    


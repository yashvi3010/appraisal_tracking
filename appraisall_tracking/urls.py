from django.contrib import admin
from django.urls import include, path
from appraisall_tracking import views
from .views import AddProject, UpdateProject, DeleteProject, DetailProject , ViewProject
from .views import DetailProjectModule, AddProjectModule, UpdateProjectModule, ViewProjectModule,  DeleteProjectModule

urlpatterns = [

    path('add/',AddProject.as_view(),name='add_project'),
    path('view/',ViewProject.as_view(),name='view_project'),
    path('<int:pk>/view/',DetailProject.as_view(),name='detail_project'),
    path('<int:pk>/delete/',DeleteProject.as_view(),name='delete_project'),
    path('<int:pk>/update/',UpdateProject.as_view(),name='update_project'),
    path('',views.sendmail, name='send_mail' ),
    path('addmodule/',AddProjectModule.as_view(),name='add_projectmodule'),
    path('viewmodule/',ViewProjectModule.as_view(),name='view_projectmodule'),
    path('<int:pk>/viewmodule/',DetailProjectModule.as_view(),name='detail_projectmodule'),
    path('<int:pk>/deletemodule/',DeleteProjectModule.as_view(),name='delete_projectmodule'),
    path('<int:pk>/updatemodule/',UpdateProjectModule.as_view(),name='update_projectmodule'),

]
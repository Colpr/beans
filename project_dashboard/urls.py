from django.urls import path
from. import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('create/', views.CreateProjectView.as_view(), name='create_project'),
    path('edit/<pk>/', views.EditProjectView.as_view(), name='edit_project'),
    path('delete/<pk>/', views.DeleteProjectView.as_view(), name='delete_project'),
]

from django.urls import path
from . import views
from .views import ListJob, Job_details, AddJobView, managePost, UpdatePost, DeletePost, categoryView, JobView, Up_LoadCV, CV_Manage, CareView, CV_POST, Search_post


urlpatterns = [
    path('',ListJob.as_view(), name='home'),
    path('Add-Jobs/',AddJobView.as_view(), name='add_post'),
    path('job_detail/<int:pk>/',Job_details.as_view(), name='post_details'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout,name='logout' ),
    path('register_tuyendung/', views.register_tuyendung, name='re_tuyendung'),
    path('managePost/', managePost.as_view(), name='managePost'),
    path('job_update/edit/<int:pk>/',UpdatePost.as_view(), name='update_post'),
    path('job_delete/<int:pk>/remove/', DeletePost.as_view(), name='delete_post'),
    path('category/<int:pk>/', categoryView, name='category'),
    path('jobview/<int:nameCompany>/', JobView, name='jobview'),
    path('UpLoadCv/<int:pk>/',Up_LoadCV.as_view(),name='upload_cv'),
    path('manage_CV/', CV_Manage.as_view(), name='manage_cv'),
    path('care/<int:pk>', CareView, name='care_view'),
    path('CV_POST/<int:pk>', CV_POST, name='cv_post'),
    path('Searched/', Search_post, name='search_post'),
]
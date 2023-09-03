from django.urls import path
from . import views
urlpatterns=[
    path('registration/',views.UserRegistrationView.as_view(),name="signUp"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/',views.UserLogoutView.as_view(),name="logout"),
    path('profile/',views.ProfileUpdateView.as_view(),name="profile"),
    path('add/projects/',views.ProjectCreateView.as_view(),name="add_projects"),
    path('projects/',views.ProjectListView.as_view(),name="projects"),
    path('project/<int:project_id>/', views.project_detail, name='project-detail'),
    path('add/resume/',views.ResumeCreateView.as_view(),name="add_resume"),
    path('resume/',views.ResumeListView.as_view(),name="resume"),
    path('add/skill/',views.SkillCreateView.as_view(),name="add_skill"),
    path('skill/',views.SkillListView.as_view(),name="skill"),
    path('add/blog/',views.BlogCreateView.as_view(),name="add_blog"),
    path('blog/',views.BlogListView.as_view(),name="blog"),
    path('contact/',views.ContactCreateView.as_view(),name="contact"),
    path('thanks/',views.Thanks.as_view(),name="thanks"),
    path('upload/picture/',views.ProfilePictureCreateView.as_view(),name="pro_pic"),
    
    # path('pictures/',views.edit_profile,name="pro"),
    # path('rate/<int:pk>/',views.RatingCreateView.as_view(),name="rate"),
    path('ratings/<int:project_id>/',views.rate_project,name="rate"),
]
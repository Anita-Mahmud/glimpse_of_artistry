from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from admin_account.forms import (BlogForm, ContactForm,  ProjectsForm, RatingForm,
    ResumeForm, SkillForm, UserProfileForm, UserRegistrationForm, UserUpdateForm)
from django.views.generic import FormView,TemplateView,ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from admin_account.models import (Blog, Contact,  Projects, Rating, Resume, Skillset,
    UserProfile)
from django.http import FileResponse


# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'signUp.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) 
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class ProfileUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home') 
        return render(request, self.template_name, {'form': form})
    

class ProjectCreateView(CreateView):
    model = Projects
    form_class = ProjectsForm
    template_name = 'add_projects.html'
    success_url = reverse_lazy('projects')
    
class ProjectListView(ListView):
    model = Projects
    template_name = 'projects.html'
    # context_object_name = 'projects'
    
    
    def get_queryset(self):
        return Projects.objects.all().order_by('-average_rating')
    
# class ProjectDetailView(DetailView):
#     model = Projects
#     template_name = 'project_detail.html'
#     context_object_name = 'i'

class ResumeCreateView(CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'add_resume.html'
    success_url = reverse_lazy('resume')
    
class ResumeListView(ListView):
    model = Resume
    template_name = 'resume.html'
    context_object_name = 'resumes'

class SkillCreateView(CreateView):
    model = Skillset
    form_class = SkillForm
    template_name = 'add_skill.html'
    success_url = reverse_lazy('skill')
    
class SkillListView(ListView):
    model = Skillset
    template_name = 'skill.html'
    context_object_name = 'skills'
    
class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add_blog.html'
    success_url = reverse_lazy('blog')
    
class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    
class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('thanks')
    
class Thanks(TemplateView):
    template_name = 'thanks.html'
    
class ProfilePictureCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'add_pic.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return redirect('home') 
        # return super().form_valid(form)
    

    
class RatingCreateView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'add_rating.html'
    # success_url = reverse_lazy('projects')
    
def rate_project(request, project_id):
    project = Projects.objects.get(pk=project_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = project
            # rating.user = request.user  
            rating.save()
            return redirect('project-detail', project_id=project.id)
    else:
        form = RatingForm()
    return render(request, 'add_rating.html', {'form': form, 'project': project})
        
def project_detail(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    ratings = project.rating_set.all()
    average_rating = (
        sum([rating.rating for rating in ratings]) / len(ratings)
        if ratings
        else 0
    )
    project.average_rating = round(average_rating, 2)
    project.save()
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = project
            rating.project.average_rating = round(average_rating, 2)
            rating.save()
            
            
            return redirect('project-detail', project_id=project_id)
    else:
        form = RatingForm()

    context = {
        'i': project,
        'ratings': ratings,
        'average_rating': round(average_rating, 2),
        'form': form,
    }
    return render(request, 'project_detail.html', context)
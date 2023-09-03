from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User
from admin_account.models import (Blog, Contact, Projects, Rating, Resume, Skillset,
    UserProfile)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password1','password2']

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email']
        
class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name','description','image','technologies','project_url','category']
        
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        
class SkillForm(forms.ModelForm):
    level = forms.CharField(max_length=100,help_text = "Enter between 10 to 100")
    class Meta:
        model = Skillset
        fields = '__all__'
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
        
class RatingForm(forms.ModelForm):
    rating = forms.CharField(max_length=100,help_text = "Enter between 0 to 7")
    class Meta:
        model = Rating
        fields = ['rating']



        
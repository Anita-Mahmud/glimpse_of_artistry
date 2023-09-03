from django.contrib import admin
from admin_account.models import Projects, Rating, Resume, Skillset, UserProfile,Blog

# Register your models here.
admin.site.register(Projects)
admin.site.register(Resume)
admin.site.register(Skillset)
admin.site.register(Rating)
admin.site.register(UserProfile)
admin.site.register(Blog)
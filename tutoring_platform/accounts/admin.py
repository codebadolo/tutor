from django.contrib import admin

# Register your models here.
from .models import CustomUser , TutorProfile , LearnerProfile 

admin.site.register(CustomUser) 
admin.site.register(LearnerProfile)
admin.site.register(TutorProfile)
from .models.enterprise import Enterprise, Module
from .models.evaluation import Assessment, TypeAssessment
from .models.employer import JobTittle, Employer, File
from django.contrib import admin

# Register your models here.
admin.site.register(Enterprise)
admin.site.register(Module)
admin.site.register(Assessment)
admin.site.register(TypeAssessment)
admin.site.register(JobTittle)
admin.site.register(File)
admin.site.register(Employer)

from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor
import models

admin.site.register(models.PersonalInfo)
admin.site.register(models.Overview)


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.Project
        widgets = {
                'summary': RedactorEditor(),
                }
        fields = "__all__"

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

admin.site.register(models.Project, ProjectAdmin)


class JobAdminForm(forms.ModelForm):
    class Meta:
        model = models.Job
        widgets = {
                'description': RedactorEditor(),
                }
        fields = "__all__"

class JobAdmin(admin.ModelAdmin):
    form = JobAdminForm

admin.site.register(models.Job, JobAdmin)


class EducationAdminForm(forms.ModelForm):
    class Meta:
        model = models.Education 
        widgets = {
                'summary': RedactorEditor(),
                }
        fields = "__all__"

class EducationAdmin(admin.ModelAdmin):
    form = EducationAdminForm

admin.site.register(models.Education, EducationAdmin)

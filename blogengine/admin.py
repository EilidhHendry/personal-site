import models
from redactor.widgets import RedactorEditor
from django.contrib import admin
from django import forms

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = models.Post
        widgets = {
                'text': RedactorEditor(),
                }
        fields = "__all__"

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(models.Post, PostAdmin)

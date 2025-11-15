from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'technology_stack', 'documentation_url', 'repository_url', 'published_date']
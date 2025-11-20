from django.shortcuts import render
from .forms import ProjectForm
from .models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()

    return render(request, "projects/projects.html", {"projects": projects})

def project_register(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "projects/projects.html")
        else:
            form = ProjectForm()
    form = ProjectForm()
  
    return render(request, "projects/adicionar.html" , {'form': form})

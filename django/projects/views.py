from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse
from projects.models import Project, PClass


def index(request, offset):
    # Mozna by chtelo zvlast passed a active
    projects = Project.objects.filter(publish=True)
    pclasses = PClass.objects.all()

    context = {
        'projects': projects,
        'pclasses' : pclasses,
    }
    return render(request, 'projects_index.html', context)

def view_project(request, slug):
    context = { 'project': get_object_or_404(Project, slug=slug),
                }
    return render(request, 'view_project.html', context)

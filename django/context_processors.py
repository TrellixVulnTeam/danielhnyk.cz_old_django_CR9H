from blog.models import Blog, Category
from projects.models import Project, PClass

def extra_context(request):
    extras = {}
    try:
        extras["ALL_CATEGS"] = Category.objects.all()
        extras["L_POSTS"] = Blog.objects.filter(publish=True).order_by("-posted")[:7]
        extras["L_PROJECTS"] = Project.objects.all().order_by("-start")[:7]
    except:
        extras["ER"] = 1

    return(extras)

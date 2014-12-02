from django import template
from blog.models import Blog, Category

register = template.Library()

@register.simple_tag
def get_pub(str_category): 
    catId = Category.objects.filter(title=str_category)[0].id
    all_pub_per_categ = Blog.objects.filter(publish=True, category=catId).order_by("-posted")
    return(all_pub_per_categ)


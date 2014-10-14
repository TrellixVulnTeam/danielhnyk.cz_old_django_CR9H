from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse
from blog.models import Blog, Category


def index(request, offset):

    if offset:
        offset = int(offset)
        if offset > 0:
            prev_of = offset - 1
        else:
            prev_of = 'no_prev'
        next_of = offset + 1
    else:
        offset = 0
        prev_of = 'no_prev'
        next_of = 1

#    actual_blogs = Blog.objects.all().order_by("-posted")[(5*offset):(5*offset+5)]
    actual_blogs = Blog.objects.filter(publish=True).order_by("-posted")[(5*offset):(5*offset+5)]

    check_length = 1
    if len(actual_blogs) == 5:
        check_length = 0
    else:
        pass

    context = {
        'posts': actual_blogs,
        'prev' : prev_of,
        'next' : next_of,
        'check_length' : check_length,
        'categories' : Category.objects.all(),
    }
    return render(request, 'blog_index.html', context)

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
         'category': category,
         'posts': Blog.objects.filter(category=category)[:5]
     }
    return render(request, 'blog_index.html', context)

def view_post(request, slug):
    context = { 'post': get_object_or_404(Blog, slug=slug),
                'cur_url': request.get_full_path(),
                }
    return render(request, 'view_post.html', context)

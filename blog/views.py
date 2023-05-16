from django.shortcuts import render
from django.template.loader import render_to_string


def myblog(request):
    return render(request, 'blog/blog.html')

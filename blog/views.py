from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from blog.models import Blog


# Create your views here.
def home_view(request):
    queryset = Blog.objects.all()
    paginator = Paginator(queryset, 25)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    template = "index.html"
    context = {
        "blogs": blogs,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(Blog, pk=pk, slug=slug)
    template = "index.html"
    return render(request, template, context={"blog": obj})

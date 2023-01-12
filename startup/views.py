from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from startup.models import Startup


# Create your views here.
def home_view(request):
    queryset = Startup.objects.all()
    paginator = Paginator(queryset, 25)
    page = request.GET.get('page')
    try:
        startup = paginator.page(page)
    except PageNotAnInteger:
        startup = paginator.page(1)
    except EmptyPage:
        startup = paginator.page(paginator.num_pages)
    template = "index.html"
    context = {
        "startups": startup,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(Startup, pk=pk, slug=slug)
    template = "index.html"
    return render(request, template, context={"startup": obj})

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from startup.models import StartUp


# Create your views here.
def home_view(request):
    queryset = StartUp.objects.all()
    paginator = Paginator(queryset, 25)
    page = request.GET.get('page')
    try:
        startups = paginator.page(page)
    except PageNotAnInteger:
        startups = paginator.page(1)
    except EmptyPage:
        startups = paginator.page(paginator.num_pages)
    template = "index.html"
    context = {
        "startups": startups,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(StartUp, pk=pk, slug=slug)
    template = "index.html"
    return render(request, template, context={"startup": obj})

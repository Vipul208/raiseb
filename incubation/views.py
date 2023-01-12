from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from startup.models import Startup

from .models import Supported_By, Team, Slider, Partner, Link
from django.template import loader
from django.core.mail import EmailMessage


# Create your views here.
def home(request):
    team = Team.objects.all()
    partner = Partner.objects.all()
    slider = Slider.objects.all().order_by('-id')
    link = Link.objects.all().order_by('-id')

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
        "sliders": slider,
        "partners": partner,
        "teams": team,
        "links": link,

        "startups": startup,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(Startup, pk=pk, slug=slug)
    template = "single-blog.html"
    return render(request, template, context={"startup": obj})


def contacts(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    msg = request.POST.get('comments')

    template = loader.get_template('contact.txt')
    data = {
        'first_name': name,
        'email': email,
        'phone': phone,
        'comments': msg
    }
    message = template.render(data)
    subject = "You've been contacted by {} {}".format(data['name'])
    email = EmailMessage(subject, message, '', ['incubation@recb.ac.in'])
    email.content_subtype = 'html'
    email.send()

    return render(request, 'hom.html', {'name': name})

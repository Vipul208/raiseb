from django.shortcuts import render
from django.template import loader
from django.core.mail import EmailMessage

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from blog.models import Blog
from .models import Testimonial, Team, Intro_video


# Create your views here.

def home(request):
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    intro = Intro_video.objects.all().order_by('-id')
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
        "teams": team,
        "testimonials": testimonial,
        "intros": intro,
    }
    return render(request, template_name=template, context=context)


def detail_view(request, pk, slug):
    obj = get_object_or_404(Blog, pk=pk, slug=slug)
    template = "single-blog.html"
    return render(request, template, context={"blog": obj})


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

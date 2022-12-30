from django.shortcuts import render
from django.template import loader
from django.core.mail import  EmailMessage

# Create your views here.

def home(request):
    return render(request, "index.html")


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

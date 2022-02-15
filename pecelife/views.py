from django.shortcuts import render, redirect
from blog.models import BlogPost
from .forms import ContactForm
from .models import Testimonial,TeamMember,Gallery,FrequentlyQuestion,Service
from django.contrib import messages
from doctor.models import Department
from django.template.loader import render_to_string
from django.core.mail import EmailMessage,send_mail
from account.models import User


# Create your views here.

def home(request):
    template_name = "index.html"
    departments = Department.objects.all()
    # posts = BlogPost.objects.all().order_by("-create_at")
    posts = BlogPost.objects.all().order_by('-id')[:3]
    testimonial_data = Testimonial.objects.all()
    gallery_images = Gallery.objects.all()
    questions = FrequentlyQuestion.objects.all()
    services = Service.objects.all()
    context = {
        'departments':departments,
        'posts':posts,
        'testimonial_data': testimonial_data,
        'gallery_images':gallery_images,
        'questions':questions,
        'services':services,
    }
    return render(request,template_name,context)



def contactView(request):
    template_name = "contact.html"
    if request.method == 'POST':
        print('fount')
        form = ContactForm(request.POST)
        if form.is_valid():
            print('vald')
            form.save()
            # mail_subject = form.cleaned_data['subject']
            # mail_messages = render_to_string('email_notification/contact_notification.html', {
            #         'name': form.cleaned_data['name'],
            #         'email': form.cleaned_data['email'],
            #         'phone': form.cleaned_data['phone'],
            #         'message': form.cleaned_data['message'],
            #     })
            # print(mail_subject)
            # # send_mail = 'siam16.m@gmail.com'
            # print('entry')
            # email = EmailMessage(
            #     mail_subject, mail_messages, to=[send_mail])
            # email.send()
            # print('sent')
            messages.success(request, 'Your Message sent Successfully.')

    form = ContactForm()
    return render(request, template_name, {'form': form})  


def teamMembersView(request):
    template_name = "team.html"
    members = TeamMember.objects.all()
    context = {
        'members': members
    }
    return render(request,template_name,context)


def testimonial(request):
    template_name = "index.html"
    data = Testimonial.objects.all()
    context ={
        'data': data
    }
    return render(request,template_name,context)
from account.models import User
from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Doctor, DoctorSchedule,Department
from .form import DoctorProfileForm, DoctorScheduleForm
from django.db.models import Q 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def doctorsView(request):
    template_name = 'doctor/doctors.html'
    search_doctor = request.GET.get('search')
    print('sdd',search_doctor)

    if search_doctor:
        quary = Q(Q(full_name__icontains=search_doctor) | Q(department__name=search_doctor) | Q(designation__icontains=search_doctor) | Q(about__icontains=search_doctor) | Q(consulting_fee__icontains=search_doctor))
        doctors = Doctor.objects.filter(quary)  
    else:
        doctors = Doctor.objects.all()
    
    page = request.GET.get('page',1)
    paginator = Paginator(doctors,8)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    departments = Department.objects.all()
    context = {
        'doctors': doctors,
        'departments':departments
    }
    return render(request, template_name, context)

def filterByDepartment(request,id):
    template_name = 'doctor/doctors.html'
    doctors = Doctor.objects.filter(department=id)
    departments = Department.objects.all()
    context = {
        'doctors': doctors,
        'departments':departments
    }
    return render(request, template_name, context)


def doctorDetailsView(request, slug):
    template_name = 'doctor/doctor-details.html'
    details = Doctor.objects.get(slug=slug)
    doctor_schedule = DoctorSchedule.objects.filter(user=details.doctor)
    print('sd',doctor_schedule)
    print('details',details)
    context = {
        'doctor': details,
        'doctor_schedule': doctor_schedule,
    }
    return render(request, template_name, context)

# def doctorDetailsView(request, slug):
#     template_name = 'doctor/doctor-details.html'
#     details = Doctor.objects.get(slug=slug)
#     doctor_schedule = DoctorSchedule.objects.filter(user=details.doctor)
#     print('sd',doctor_schedule)
#     # print('details',details)
#     print('details',details)
#     context = {
#         'doctor': details,
#         'doctor_schedule': doctor_schedule,
#     }
#     return render(request, template_name, context)


# only for authenticated doctors
def DoctorProfileView(request):
    if request.user.is_authenticated and request.user.user_type=='Doctor':
        template_name = 'dashboard/profile_update.html'
        doctor_profile = Doctor.objects.filter(doctor=request.user)
        doctor_schedule = DoctorSchedule.objects.filter(user=request.user)
        # print('Doctor',doctor_schedule)
        context = {
            'doctor_profile': doctor_profile,
            'doctor_schedule': doctor_schedule,
            'user_active': 'navbar-active-color',
            'pro_active': 'bg-primary text-white'
        }

        return render(request, template_name, context)
    else:
        return redirect('home')

# only for authenticated doctors


def doctorProfileUpdateview(request):
    if request.user.is_authenticated and request.user.user_type=='Doctor':
        template_name = 'dashboard/profile-edit.html'
        if request.method == 'POST':
            doctor_exists = Doctor.objects.filter(
                doctor=request.user).exists()
            if doctor_exists:
                doctor = Doctor.objects.get(doctor=request.user)
                form = DoctorProfileForm(
                    request.POST, request.FILES, instance=doctor)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
            else:
                form = DoctorProfileForm(request.POST or None, request.FILES)
                if form.is_valid():
                    print('name',request.user)
                    print('username',request.User.username)
                    doctor = request.user.username
                    full_name = form.cleaned_data['full_name']
                    department = form.cleaned_data['department']
                    designation = form.cleaned_data['designation']
                    about = form.cleaned_data['about']
                    education = form.cleaned_data['education']
                    experience = form.cleaned_data['experience']
                    consulting_fee = form.cleaned_data['consulting_fee']
                    image = request.FILES['image']
                    print('image', image)
                    data = Doctor(doctor=doctor, full_name=full_name, department=department, designation=designation,
                                         about=about, education=education, experience=experience,consulting_fee=consulting_fee, image=image)
                    data.save()
                    return redirect('profile')
        else:
            doctor_exists = Doctor.objects.filter(
                doctor=request.user).exists()
            if doctor_exists:
                doctor = Doctor.objects.get(doctor=request.user)
                form = DoctorProfileForm(instance=doctor)
                context = {
                    'form': form,
                    'user_active': 'navbar-active-color',
                    'up_active': 'bg-primary text-white'
                }
            else:
                form = DoctorProfileForm()
                context = {'form': form}
            return render(request, template_name, context)

# only for authenticated doctors


def DoctorScheduleView(request):
    if request.user.is_authenticated and request.user.user_type=='Doctor':
        template_name = 'doctor/doctor_schedule.html'
        if request.method == 'POST':
            form = DoctorScheduleForm(request.POST or None)
            if form.is_valid():
                print('valid')
                user = request.user
                day = form.cleaned_data['day']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                data = DoctorSchedule(user=user, day=day,
                                      start_time=start_time, end_time=end_time)
                data.save()
                messages.success(request, 'Schedule added successfully.')
            return redirect('add-schedule')
        else:
            form = DoctorScheduleForm()
            doctor_schedule = DoctorSchedule.objects.filter(user=request.user)
            context = {
                'form': form,
                'doctor_schedule': doctor_schedule,
                'user_active': 'navbar-active-color',
                'ad_active': 'bg-primary text-white'
            }
            return render(request, template_name, context)
    return redirect('profile')

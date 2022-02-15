from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.views import View
from .models import PatientProfile
from .form import PatientProfileForm



# only for authenticated patients
def patientProfileView(request):
    if request.user.is_authenticated and request.user.is_patient:
        template_name = 'patient/patient_profile.html'
        patient_profile = PatientProfile.objects.filter(patient=request.user)
        # print('patient',patient_schedule)
        context ={
            'patient_profile':patient_profile,
            'user_active':'navbar-active-color',
            'pro_active':'bg-primary text-white'
            }

        return render(request,template_name,context)
    else:
        return redirect('home')

# only for authenticated patients
def patientProfileUpdateview(request):
    if request.user.is_authenticated and request.user.is_patient:
        template_name = 'patient/patient_profile_update.html'
        if request.method == 'POST':
            patient_exists = PatientProfile.objects.filter(patient=request.user).exists()
            if patient_exists:
                patient = PatientProfile.objects.get(patient=request.user)
                form = PatientProfileForm(request.POST,request.FILES,instance=patient)
                if form.is_valid():
                    form.save()
                    return redirect('patient_profile')
            else:
                form = PatientProfileForm(request.POST or None,request.FILES)
                if form.is_valid():
                    patient = request.user
                    name = form.cleaned_data['name']
                    about = form.cleaned_data['about']
                    image = request.FILES['image']
                    data = PatientProfile(patient=patient, name=name,about=about,image=image )
                    data.save()
                    return redirect('patient_profile')
        else:
            patient_exists = PatientProfile.objects.filter(patient=request.user).exists()
            if patient_exists:
                patient = PatientProfile.objects.get(patient=request.user)
                form = PatientProfileForm(instance=patient)
                context = {
                    'form': form,
                    'user_active': 'navbar-active-color',
                    'up_active': 'bg-primary text-white'
                    }
            else:
                form = PatientProfileForm()
                context = {'form': form}
            return render(request, template_name,context)

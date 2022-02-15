from django.shortcuts import render,redirect
from doctor.models import Doctor,Department,DoctorSchedule
from doctor.form import DoctorProfileForm

# Create your views here.

def profileView(request):
    if request.user.is_authenticated:
        template_name = "dashboard/users-profile.html"
        context ={}
        if request.user.user_type=='Doctor':
            doctor_profile = Doctor.objects.filter(doctor=request.user)
            doctor_schedule = DoctorSchedule.objects.filter(user=request.user)
            context = {
                'doctor_profile': doctor_profile,
                'doctor_schedule': doctor_schedule,
            }
        
        return render(request,template_name,context)


def profileUpdateView(request):
    if request.user.is_authenticated and request.user.user_type=='Doctor':
        template_name = "dashboard/profile_update.html"
        form = DoctorProfileForm()
        context = {'form': form}
        print('user is ',request.user)
        if request.method == 'POST':
            print('user is enter post')
            doctor_exists = Doctor.objects.filter(doctor=request.user).exists()
            if doctor_exists:
                print('user is enter exts')
                doctor = Doctor.objects.get(doctor=request.user)
                form = DoctorProfileForm(request.POST, request.FILES, instance=doctor)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
            else:
                print('user is else mal post')
                form = DoctorProfileForm(request.POST or None, request.FILES)
                doctor = request.user
               # print('user is', form)
                # full_name = form.cleaned_data['full_name']
                # department = form.cleaned_data['department']
                # designation = form.cleaned_data['designation']
                # about = form.cleaned_data['about']
                # education = form.cleaned_data['education']
                # experience = form.cleaned_data['experience']
                # consulting_fee = form.cleaned_data['consulting_fee']


                if form.is_valid():
                    # print('user is valid post')
                    # print('Usrnaaem',request.user.username)
                    # print('name',request.user)
                    
                
                    full_name = form.cleaned_data['full_name']
                    department = form.cleaned_data['department']
                    #print(department)
                    designation = form.cleaned_data['designation']
                    about = form.cleaned_data['about']
                    education = form.cleaned_data['education']
                    experience = form.cleaned_data['experience']
                    consulting_fee = form.cleaned_data['consulting_fee']
                    image = request.FILES['image']

                    data = Doctor(doctor=doctor, full_name=full_name, department=department, designation=designation,
                                            about=about, education=education, experience=experience,consulting_fee=consulting_fee, image=image)
                    data.save()
                    print('save')
                    return redirect('profile')
                else:
                    print("dhuki nai")
        else:
            print('mals te')
            doctor_exists = Doctor.objects.filter(doctor=request.user).exists()
            if doctor_exists:
                doctor = Doctor.objects.get(doctor=request.user)
                form = DoctorProfileForm(instance=doctor)
                context = {
                    'form': form,
                    # 'user_active': 'navbar-active-color',
                    # 'up_active': 'bg-primary text-white'
                }
        return render(request,template_name,context)
    return redirect('profile')
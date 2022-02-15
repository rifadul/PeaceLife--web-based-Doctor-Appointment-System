from django.shortcuts import render, redirect
# from django.contrib.auth.forms import 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.views import View

# Create your views here.

def signupView(request):
    if not request.user.is_authenticated:
        template_name = 'account/signup.html'
        context = {}

        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                messages.SUCCESS(request, 'Account Create Successfully! Please Login.')
                user = form.save()
                return redirect('login')
            else:
                messages.error(request, 'Please enter your valid information.')
                form = SignupForm()
                context = {
                'forms': form
                }
        else:
            form = SignupForm()
            context = {
                'forms': form
                }
        return render(request, template_name , context)
    else:
        return redirect('profile')


# class SignInView(LoginView):
#         # form_class = LoginForm
#         template_name = 'account/login.html'

class LoginView(View):
        template_name = 'account/login.html'
        def get(self, request, *args, **kwargs):
            form = LoginForm()
            context = {
                'form': form
                }
            return render(request,self.template_name,context)

        def post(self, request, *args, **kwargs):
            context={
                'data': request.POST,
                'has_error': False
            }
            username = request.POST.get('email')
            password = request.POST.get('password')
            if username =='':
                messages.add_message(request,messages.ERROR,'Username is required')
                context['has_error'] = True
            if password == '':
                messages.add_message(request,messages.ERROR,'Password is required')
                context['has_error'] = True

            user = authenticate(username=username,password=password)
            if not user and not context['has_error']:
                messages.add_message(request,messages.ERROR,'Invalid username or password')
                context['has_error'] = True

            if context['has_error']:
                form = LoginForm()
                context = {
                'form': form
                }
                return render(request,self.template_name,context)
            
            login(request,user)
            return redirect('home')



class logoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Account logout Successfully')
            return redirect('login')
        else:
            return redirect('profile')
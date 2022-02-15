from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment,PaymentDetails
from doctor.models import Doctor
from .form import AppointmentForm,ConfirmationStatusForm
from subscription.models import Subscription
from django.shortcuts import get_object_or_404
import uuid
from django.views.decorators.csrf import csrf_exempt

# payment 
import requests
import socket
from django.urls import reverse
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

def appointmentView(request):
    if request.user.is_authenticated:
        template_name = 'appointment/appointment.html'
        form = AppointmentForm()
        
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            try:
                subscribe = Subscription.objects.get(name=request.user)
                print(subscribe.subscribe)
            except:
                subscribe = False

            if form.is_valid():
                doc = Doctor.objects.get(slug=request.GET['doctorname'])
                user = request.user
                doctor = doc
                appointment_id = str(uuid.uuid4())
                patient_name = form.cleaned_data['patient_name']
                gender = form.cleaned_data['gender']
                age = form.cleaned_data['age']
                mobile = request.user.phone
                email = request.user.email
                problem_brief = form.cleaned_data['problem_brief']
                appointment_type = form.cleaned_data['appointment_type']
                appointment_date = form.cleaned_data['appointment_date']

                if not subscribe:
                    # payment instance create for payment details save
                    payment_person = patient_name
                    transaction_id = str(uuid.uuid4())
                    amount = doc.consulting_fee
                    card_type = ''
                    payment_status = 'Pending'
                    transaction_date = ''
                    risk_title = ''
                    payment = PaymentDetails(payment_person=payment_person,transaction_id=transaction_id,amount=amount,card_type=card_type,payment_status=payment_status,transaction_date=transaction_date,risk_title=risk_title)
                    payment.save()
                    data = Appointment(user=user, doctor=doctor,payment=payment,appointment_id=appointment_id, patient_name=patient_name, gender=gender,age=age, mobile=mobile, email=email, problem_brief=problem_brief, appointment_type=appointment_type,appointment_date=appointment_date)
                    data.save()
                
                # payment
                    store_id = 'pecel616d784f482e9'
                    store_password = 'pecel616d784f482e9@ssl'
                    payment_status_url = f"http://127.0.0.1:8000/appointment/status/{appointment_id}/{transaction_id}/"

                    print(payment_status_url)
                    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_password)

                    mypayment.set_urls(success_url=payment_status_url, fail_url=payment_status_url, cancel_url=payment_status_url, ipn_url=payment_status_url)

                    mypayment.set_product_integration(total_amount=Decimal(amount), currency='BDT', product_category='Mixed ', product_name='doctor', num_of_item=1, shipping_method='YES', product_profile='None')

                    mypayment.set_customer_info(name=patient_name, email=email, address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone=mobile)

                    mypayment.set_shipping_info(shipping_to=patient_name, address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')

                    response_data = mypayment.init_payment()
                    print (response_data)
                    return redirect(response_data['GatewayPageURL'])
                else:
                    pay_status = True
                    payment_person = patient_name
                    transaction_id = str(uuid.uuid4())
                    amount = doc.consulting_fee
                    card_type = 'Subscriber'
                    payment_status = 'VALID'
                    transaction_date = ''
                    risk_title = 'Safe'
                    payment = PaymentDetails(payment_person=payment_person,transaction_id=transaction_id,amount=amount,card_type=card_type,payment_status=payment_status,transaction_date=transaction_date,risk_title=risk_title)
                    payment.save()
                    data = Appointment(user=user, doctor=doctor,payment=payment,appointment_id=appointment_id, patient_name=patient_name, gender=gender,age=age, mobile=mobile, email=email, problem_brief=problem_brief, appointment_type=appointment_type,appointment_date=appointment_date,pay_status=pay_status)
                    data.save()
                    return redirect('appointment-list')
        else:
            context ={
                'form':form
            }
            return render(request, template_name,context)
    else:
        return redirect('login')


def appointmentListView(request):
    if request.user.is_authenticated and request.user.user_type=='Doctor' or request.user.user_type=='Patient':
        template_name = "appointment/appointment_list.html"
        if request.user.user_type=='Doctor':
            print("ase nai",request.user.user_type)
            doctor = Doctor.objects.get(doctor=request.user)
            print("ase nai",request.user.user_type)
            appointment_list = Appointment.objects.filter(doctor=doctor)

        elif request.user.user_type=='Patient':
            appointment_list = Appointment.objects.filter(user=request.user).order_by('-id')

        context = {
            'appointment_list': appointment_list,
        }
        return render(request, template_name, context)
    else:   
        return redirect('login')


def appointmentConfirmation(request,slug):
    if request.user.is_authenticated and request.user.user_type=='Doctor':
        template_name = "appointment/appointment_confirmation.html"
        obj = get_object_or_404(Appointment, slug=slug)
        form = ConfirmationStatusForm(request.POST or None, instance=obj)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('appointment-list')
        else:
            context = {'form':form}
            return render(request, template_name, context)
    else:
        return redirect('login')


@csrf_exempt
def payment_status(request,appointment,pay):
    appointment = appointment
    pay = pay
    payment_data = request.POST
    status = payment_data['status']
    print('vkndkfv cjek',status)
    template_name ="payment/payment_status.html"   
    if request.method == 'POST' or request.method == 'post':
        if status=='VALID':
            transaction_id = payment_data['tran_id']
            card_type = payment_data['card_type']
            status = payment_data['status']
            transaction_date = payment_data['tran_date']
            risk_title = payment_data['risk_title']


            # updating payment
            payment = PaymentDetails.objects.get(transaction_id=pay)
            payment.transaction_id = transaction_id
            payment.card_type = card_type
            payment.payment_status = status
            payment.transaction_date = transaction_date
            payment.risk_title = risk_title
            payment.save()
            appointment = Appointment.objects.get(appointment_id=appointment)
            appointment.pay_status = True
            appointment.save()
            context={
                'success':True,
            }
            return render(request,template_name,context)
        context={
            'success':False,
        }
        return render(request,template_name,context)






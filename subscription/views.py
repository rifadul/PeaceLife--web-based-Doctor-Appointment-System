from django.shortcuts import render,HttpResponse,redirect
from .models import PricePlan,Subscription
import uuid
from appointment.models import PaymentDetails
from django.views.decorators.csrf import csrf_exempt

# payment 
import requests
import socket
from django.urls import reverse
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

# Create your views here.

def subscriptionPackageView(request):
    template_name = "subscription/subscription.html"
    plans = PricePlan.objects.all()
    context = {
        'plans': plans,
    }
    return render(request,template_name,context)


def subscriptionView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            plans = PricePlan.objects.get(id=request.POST.get('plan_id'))
            name = request.user
            email =  request.user.email
            mobile = request.user.phone
            print(name,email,mobile)
            plan_name = plans.plan_name
            subscription_id = str(uuid.uuid4())
            plan_price = plans.plan_price

            # payment instance create for payment details save
            payment_person = request.user.full_name()
            transaction_id = str(uuid.uuid4())
            amount = plan_price*12
            card_type = ''
            payment_status = 'Pending'
            transaction_date = ''
            risk_title = ''
            payment = PaymentDetails(payment_person=payment_person,transaction_id=transaction_id,amount=amount,card_type=card_type,payment_status=payment_status,transaction_date=transaction_date,risk_title=risk_title)
            payment.save()
            print("ami asi")
            data = Subscription(name=name, plan_name=plan_name,payment=payment,subscription_id=subscription_id, plan_price=plan_price)
            data.save()
            print("ami asi 2")

            store_id = 'pecel616d784f482e9'
            store_password = 'pecel616d784f482e9@ssl'
            payment_status_url = f"http://127.0.0.1:8000/subscription/status/{subscription_id}/{transaction_id}/"

            print(payment_status_url)
            mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_password)
            print("ami asi 3")
            mypayment.set_urls(success_url=payment_status_url, fail_url=payment_status_url, cancel_url=payment_status_url, ipn_url=payment_status_url)
            print("ami asi 4")

            mypayment.set_product_integration(total_amount=Decimal(amount), currency='BDT', product_category='Mixed ', product_name='Subscription Package', num_of_item=1, shipping_method='YES', product_profile='None')

            mypayment.set_customer_info(name=payment_person, email=email, address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone=mobile)

            mypayment.set_shipping_info(shipping_to=payment_person, address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')
            print("ami asi 5")
            response_data = mypayment.init_payment()
            print (response_data)
            print("ami asi 6")
            return redirect(response_data['GatewayPageURL'])
        else:
            return redirect('subscription')




@csrf_exempt
def subscription_payment_status(request,subscription,trans_id):
    subscription = subscription
    trans_id = trans_id
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
            payment = PaymentDetails.objects.get(transaction_id=trans_id)
            payment.transaction_id = transaction_id
            payment.card_type = card_type
            payment.payment_status = status
            payment.transaction_date = transaction_date
            payment.risk_title = risk_title
            payment.save()
            subscription = Subscription.objects.get(subscription_id=subscription)
            subscription.subscribe = True
            subscription.save()
            context={
                'success':True,
            }
            return render(request,template_name,context)
        context={
            'success':False,
        }
        return render(request,template_name,context)
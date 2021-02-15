from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
import smtplib


def contacts(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        property = request.POST['property']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtors_email = request.POST['realtors_email']

        # Check User Has Made Inquiry Already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(property_id=property_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You Are Already Made an Inquiry For This Listing")
                return redirect('/properties/' + property_id)

        contact = Contact(property_id=property_id, property=property,  name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # send email
        send_mail(
            'Property Listing Inquiry',
            'There Has Been an Inquiry For ' + '. Sign into the admin panel for more info',
            'meetsoni704648@gmail.com',
            [realtors_email, 'ravison455@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "Your Request Has Been Submitted, A Realtor Will Get Back To You Soon")
        return redirect('/properties/' + property_id)

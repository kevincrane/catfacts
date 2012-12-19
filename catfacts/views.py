from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from random import choice
from django.utils import timezone
import re
import logging

from catfacts.models import Fact, Email_User, Phone_User


logger = logging.getLogger(__name__)


# Home page view
def home(request):
    facts = Fact.objects.all()
    context = {'rand_fact': choice(facts)}
    return render(request, 'catfacts/home.html', context)

# FAQ page view
def faq(request):
    return render(request, 'catfacts/faq.html')

# About page view
def about(request):
    return render(request, 'catfacts/about.html')


# Add new user to models; POST method
def new_user(request):
    PREV_PAGE = "catfacts/home.html"

    # Try to read the user's name and contact method from POST
    try:
        if not (request.POST.get('name') and request.POST.get('contact')):
            raise KeyError
        user_name = request.POST['name']
        user_contact = request.POST['contact']
    except KeyError:
        return render(request, PREV_PAGE, {
            'error_message': "Make sure to enter your name and email/phone number.",
            })

    # TODO: test what type of input this is

    # Add user to DB if applicable
    email_address = re.search(r"[^@]+@[^@]+\.[^@]+", user_contact)
    phone_number = re.search(r'(\d{3})\D*(\d{3})\D*(\d{4})', user_contact)
    if email_address:
        email_user = Email_User(name=user_name,
                                email=email_address.group(0),
                                date_joined=timezone.now(),
                                valid=True)
        email_user.save()
        return HttpResponseRedirect("/")

    elif phone_number and len(phone_number.groups()) == 3:
        email_user = Phone_User(name=user_name,
            phone=phone_number.group(1) + phone_number.group(2) + phone_number.group(3),
            date_joined=timezone.now(),
            valid=True)
        email_user.save()
        return HttpResponseRedirect("/")

    else:
        # User is stupid and can't type an email or phone number properly
        return render(request, PREV_PAGE, {
            'error_message': "I couldn't tell if that was an email or phone number. Want to try that again?",
            })


# TODO: Link so people can submit own CatFacts.
#   - New view, just instructions, name box, bigger textbox
#   - Submitting passes that text to Django as POST argument
#   - Generates very short email with common subject line and catfact as body
#   - Profit

# TODO: Make unsubscribe page
#   - Send POST request to unsubscribe.html with email address
#   - HTML: $email has been unsubscribed!
#   - view: load models where email=$email, set valid=false

# TODO: Set up daily cron job
#   - import model from Python
#   - Load, pick random fact, send email, repeat

# TODO: Maybe confirmation emails

# TODO: Javascript/AJAX for removing text boxes and only updating center of page on page change
import os

import requests
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
# Create your views here.

def verify_token(token, ip):
    url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"

    data = {"secret": settings.TURNSTILE_SECRET_KEY, "response": token, "remoteip": ip}

    response = requests.post(url, json=data)

    outcome = response.json()
    if outcome.get("success", False):
        return True
    else:
        return False

class AboutView(TemplateView):
    template_name = "pages/about/version_1.html"



class ContactView(TemplateView):
    template_name = "pages/contact/version_1.html"

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST["name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            message = request.POST["message"]
        except KeyError:
            return render(
                request,
                self.template_name,
                {"error_message": "Please fill out all required fields."},
            )
        try:
            details = request.POST["details"]
        except KeyError:
            details = False

        if not verify_token(
            request.POST["cf-turnstile-response"], request.META["REMOTE_ADDR"]
        ):
            subject = "Spam Alert"
            from_email = settings.EMAIL_HOST_USER
            to = ["akib@mibiome.com"]
            send_mail(
                subject,
                f"Hi There\n{name} with email {email} and contact number as {phone} has an enquiry as follows:\n{message}\n Details:{details}",
                from_email,
                to,
            )
        else:
            subject = "Enquiry"
            from_email = settings.EMAIL_HOST_USER
            to = [
                "akib@mibiome.com",
                "datahelixai@mibiome.com",
                "research@mibiome.com",
                "trideep@mibiome.com",
            ]
            send_mail(
                subject,
                f"Hi There\n{name} with email {email} and contact number as {phone} has an enquiry as follows:\n{message}",
                from_email,
                to,
            )
        return render(
            request,
            self.template_name,
            {"success_message": "Your enquiry has been successfully sent."},
        )


class HomeView(TemplateView):
    template_name = "pages/home/version_1.html"


class ResearchView(TemplateView):
    template_name = "pages/research/version_1.html"

class ResearchAreaView(TemplateView):
    template_name = "pages/research/version_2.html"


class ServicesView(TemplateView):
    template_name = "pages/genomics/version_1.html"


def pki(request):
    fileLocation = f"{os.getcwd()}/4C9A034B553DA5F76D9EF5851892591B.txt"
    try:
        with open(fileLocation, "r") as f:
            file_data = f.read()

        # sending response
        response = HttpResponse(file_data, content_type="text/plain")
        response["Content-Disposition"] = (
            f"attachment; filename=4C9A034B553DA5F76D9EF5851892591B.txt"
        )

    except Exception as ex:
        # handle file not exist case here
        response = HttpResponseNotFound(f"Error finding file: {str(ex)}")

    return response


class TermsAndConditionsView(TemplateView):
    template_name = "pages/terms/version_1.html"


def error_404(request, exception):
    data = {}
    return render(request, "pages/404.html", data)


def error_500(request):
    data = {}
    return render(request, "pages/500.html", data)
from django.shortcuts import render, get_object_or_404
from .models import TestimonyMsg
from .models import CompanyProfile
from django.utils.translation import gettext as _, get_language


# Create your views here.
def index(request):
    lang = get_language()
    testimonies = TestimonyMsg.objects.filter(lang=lang)
    title = _("Redo Developers Inc. | Pioneering Technology Solutions for Success")
    description = _(
        "Discover a transformative partnership with Redo Developers Inc. We're your trailblazing ally, delivering cutting-edge technology and innovative software solutions to propel businesses and individuals towards success in the dynamic digital landscape."
    )
    context = {
        "testimonies": testimonies,
        "title": title,
        "description": description,
    }
    return render(request, "main/index.html", context)


def about_company(request):
    context = {
        "title": "About Redo Developers Inc. | Pioneering Innovation in Software and Technological services.",
        "description": "Explore the journey of Redo Developers Inc. – where vision meets innovation. Learn about our commitment to reshaping the digital landscape, crafting software solutions that transcend boundaries, and our impact on industries and society.",
    }
    return render(request, "main/about.html", context)


def company_profiles(request):
    profiles = CompanyProfile.objects.all()
    title = "Company Profiles | Redo Developers Inc."
    description = "Explore profiles of individuals working at Redo Developers Inc. Discover the talented team behind our cutting-edge technology and innovative solutions driving success in today's digital landscape."
    context = {"title": title, "description": description, "profiles": profiles}
    return render(request, "main/profiles.html", context)


def profile_detail(request, slug):
    profile = get_object_or_404(CompanyProfile, slug=slug)
    roles = profile.position.all()

    role_names = ", ".join(role.name for role in roles)

    title = f"As a {role_names}, Learn more about {profile.name}'s Life, roles and contributions at Redo Developers Inc."

    description = f"{profile.name},"
    context = {"profile": profile, "title": title, "description": description}
    return render(request, f"main/{profile.template_name}.html", context)


def company_services(request):
    title = "Our Services | Redo Developers Inc."
    description = "Explore the comprehensive range of services offered by Redo Developers Inc. We specialize in innovative solutions tailored to meet your needs."
    context = {"title": title, "description": description}
    return render(request, "main/services.html", context)


def contact_us(request):
    title = "Contact Us | Redo Developers Inc."
    description = "Get in touch with Redo Developers Inc. for inquiries, partnerships, or any assistance you may need. We're here to help!"
    context = {"title": title, "description": description}
    return render(request, "main/contact.html", context)

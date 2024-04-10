from django.shortcuts import render, get_object_or_404
from .models import CompanyProfile, Testimony
from django.templatetags.static import static
from django.conf import settings


# Create your views here.
def index(request):
    testimonies = Testimony.objects.all()
    title = f"{settings.APP_NAME} | Pioneering Technology Solutions for Success"
    description = f"Discover a transformative partnership with {settings.APP_NAME} We're your trailblazing ally, delivering cutting-edge technology and innovative software solutions to propel businesses and individuals towards success in the dynamic digital landscape."
    context = {
        "testimonies": testimonies,
        "title": title,
        "description": description,
    }
    return render(request, "main/index.html", context)


def about_company(request):
    context = {
        "title": f"About {settings.APP_NAME} | Pioneering Innovation in Software and Technological services.",
        "description": f"Explore the journey of {settings.APP_NAME} – where vision meets innovation. Learn about our commitment to reshaping the digital landscape, crafting software solutions that transcend boundaries, and our impact on industries and society.",
    }
    return render(request, "main/about.html", context)


def company_profiles(request):
    profiles = CompanyProfile.objects.all()
    title = f"Company Profiles | {settings.APP_NAME}"
    description = f"Explore profiles of individuals working at {settings.APP_NAME} Discover the talented team behind our cutting-edge technology and innovative solutions driving success in today's digital landscape."
    context = {"title": title, "description": description, "profiles": profiles}
    return render(request, "main/profiles.html", context)


def profile_detail(request, slug):
    profile = get_object_or_404(CompanyProfile, slug=slug)
    roles = profile.position.all()

    role_names = ", ".join(role.name for role in roles)

    title = f"As a {role_names}, Learn more about {profile.name}'s Life, roles and contributions at {settings.APP_NAME}"

    description = f"{profile.name},"
    context = {"profile": profile, "title": title, "description": description}
    return render(request, f"main/{profile.template_name}.html", context)


def company_services(request):
    title = f"Our Services | {settings.APP_NAME}"
    description = f"Explore the comprehensive range of services offered by {settings.APP_NAME} We specialize in innovative solutions tailored to meet your needs."
    context = {"title": title, "description": description}
    return render(request, "main/services.html", context)


def contact_us(request):
    title = f"Contact Us | {settings.APP_NAME}"
    description = f"Get in touch with {settings.APP_NAME} for inquiries, partnerships, or any assistance you may need. We're here to help!"
    context = {"title": title, "description": description}
    return render(request, "main/contact.html", context)


def investments(request):
    brand = "FinGuard"
    title = (
        f"Unlock Financial Freedom: Navigate the Market Maze with Confidence | {brand}"
    )
    image = static("images/invest.png")
    type = "article"
    description = f"Discover the path to financial security with {brand}. Our expertly managed investment platform offers a roadmap through the market maze, ensuring consistent growth and stability. Join us today and seize control of your financial future!"
    context = {
        "brand": brand,
        "title": title,
        "description": description,
        "image": image,
        "type": type,
    }
    return render(request, "main/investments.html", context)

from django.contrib import admin
from .models import Testimony, CompanyProfile, CompanyRole
from django import forms
from base.widget import CheckboxSelectMultipleWidget

# Register your models here.


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = "__all__"
        widgets = {
            "position": CheckboxSelectMultipleWidget(),
        }


class CompanyProfileAdmin(admin.ModelAdmin):
    form = CompanyProfileForm


admin.site.register(CompanyProfile, CompanyProfileAdmin)


admin.site.register(Testimony)
admin.site.register(CompanyRole)

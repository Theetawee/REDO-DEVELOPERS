from django.contrib import admin
from .models import Testimony, CompanyProfile, CompanyRole, TestimonyMsg

# Register your models here.


admin.site.register(Testimony)
admin.site.register(CompanyProfile)
admin.site.register(CompanyRole)
admin.site.register(TestimonyMsg)

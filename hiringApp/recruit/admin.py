from django.contrib import admin
from .models import Response, CvTemplate, Requirement
# Register your models here.
admin.site.register(Response)
admin.site.register(CvTemplate)
admin.site.register(Requirement)

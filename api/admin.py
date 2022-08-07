from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(QrCodes)
admin.site.register(Viewer)
admin.site.register(Viewed_Qr_code)
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin

from .models import destination,watches,cloth,shoes,perfumes,popular

# Register your models here.
admin.site.register(popular)
admin.site.register(destination)
admin.site.register(watches)
admin.site.register(cloth)
admin.site.register(shoes)
admin.site.register(perfumes)


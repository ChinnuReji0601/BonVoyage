from django.contrib import admin

from tour.models import Package, Aboutus, Contactus, Terms, Enquiry, Register, TablePayment

# Register your models here.

admin.site.register(Package)
admin.site.register(Aboutus)
admin.site.register(Contactus)
admin.site.register(Terms)
admin.site.register(Enquiry)
admin.site.register(Register)
admin.site.register(TablePayment)
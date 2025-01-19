from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('login/',views.login,name='login'),
    path('package/',views.package,name='package'),
    path('payment/<int:package_id>/', views.payment_view, name='payment'),
    path('register/',views.register,name='register'),
    path('terms/',views.terms,name='terms'),
    path('book/<int:package_id>/', views.book, name='book'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('aboutuslog/',views.aboutuslog,name='aboutuslog'),
    path('contactuslog/',views.contactuslog,name='contactuslog'),
    path('enquirylog/',views.enquirylog,name='enquirylog'),
    path('packagelog/',views.packagelog,name='packagelog'),
    path('termslog/',views.termslog,name='termslog'),
    path('booklog/<int:package_id>/', views.booklog, name='booklog'),
    path('thank_youlog/',views.thank_youlog,name='thank_youlog'),
    path('tablepayment/',views.table_payment_view,name='tablepayment'),
    path('bookings/',views.bookings,name='bookings'),
    path('payment_success/',views.payment_success,name='payment_success')
]
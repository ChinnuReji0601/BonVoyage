from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from tour.forms import EnquiryForm
from tour.models import Package, Aboutus, Contactus, Terms, Register, TablePayment


# Create your views here.


def home(request):
    return render(request,'home.html')

def aboutus(request):
    about = Aboutus.objects.first()
    return render(request, 'aboutus.html', {'about': about})
def aboutuslog(request):
    about = Aboutus.objects.first()
    return render(request, 'aboutuslog.html', {'about': about,'username': request.user.username})


def contactus(request):
    contact = Contactus.objects.first()
    return render(request, 'contactus.html', {'contact': contact})
def contactuslog(request):
    contact = Contactus.objects.first()
    return render(request, 'contactuslog.html', {'contact': contact,'username': request.user.username})

def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            # You can redirect to a thank-you page or send a success message
            return render(request, 'thank_you.html')  #
    else:
        form = EnquiryForm()

    return render(request, 'enquiry.html', {'form': form})
def enquirylog(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            # You can redirect to a thank-you page or send a success message
            return render(request, 'thank_youlog.html')  #
    else:
        form = EnquiryForm()

    return render(request, 'enquirylog.html', {'form': form,'username': request.user.username})

def thank_you(request):
    return render(request,'thank_you.html')
def thank_youlog(request):
    return render(request,'thank_youlog.html')



def package(request):
    packages=Package.objects.all()
    return render(request,'package.html',{'packages':packages})
def packagelog(request):
    packages=Package.objects.all()
    return render(request,'packagelog.html',{'packages':packages,'username': request.user.username})

def book(request, package_id):
    package = get_object_or_404(Package, id=package_id)  # Fetch the specific package using the ID
    return render(request, 'book.html', {'package': package})




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return redirect("register")
            else:
                k = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )

                subject = "Congratulations you are successfully registered"
                message = f"{k.first_name} {k.last_name} ,thankyou for registering"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [k.email]
                send_mail(subject, message, email_from, recipient_list)

                ok = Register()
                ok.us = k
                ok.phone = request.POST['phone']
                ok.gender = request.POST['gender']
                ok.save()
                return redirect("login")
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            k = User.objects.get(username=username)
            if k.check_password(password):
                if k:
                    auth.login(request, k)
                    return redirect('dashboard')
                else:
                    return render(request, 'login.html', {'error': "user does not exist"})
            else:
                return render(request, 'login.html', {'error': "password is incorrect"})
        else:
            return render(request, 'login.html', {'error': "username already exists"})
    else:
        return render(request, 'login.html', {'error': 'method is not post'})


def dashboard(request):
    return render(request, 'dashboard.html', {'username': request.user.username})


def logout(request):
    auth.logout(request)
    return redirect('register')


def terms(request):
    term=Terms.objects.first()
    return render(request,'terms.html',{'term':term})
def termslog(request):
    term=Terms.objects.first()
    return render(request,'termslog.html',{'term':term,'username': request.user.username})

def tablepayment(request):
    return render(request,'tablepayment.html')

def bookings(request):
    payments = TablePayment.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'payments': payments})

def booklog(request, package_id):
    package = get_object_or_404(Package, id=package_id)  # Fetch the specific package using the ID
    return render(request, 'booklog.html', {'package': package})

def payment_view(request, package_id):
    package = get_object_or_404(Package, id=package_id)  # Fetch the package by ID
    total_price = request.POST.get('total_price')  # Get total price from the form

    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        payment_method = request.POST.get('payment')  # Payment method (credit/debit card)
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Check if all necessary fields are present
        if not first_name or not last_name or not email or not payment_method:
            return render(request, 'payment.html', {'error': 'Please fill in all fields.', 'package': package, 'total_price': total_price})

        # Create new payment record associated with the logged-in user
        TablePayment.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            payment_method=payment_method,
            card_number=card_number,
            expiry_date=expiry_date,
            cvv=cvv,
            total_price=total_price,
            package=package,
            user=request.user  # Associate payment with the logged-in user
        )

        # Redirect to a success page or the table showing all payments
        return redirect('payment_success')

    return render(request, 'payment.html', {'package': package, 'total_price': total_price})

def payment_success(request):
    return render(request,'payment_success.html')

def table_payment_view(request):
    payments = TablePayment.objects.filter(user=request.user)
    return render(request, 'tablepayment.html', {'payments': payments})
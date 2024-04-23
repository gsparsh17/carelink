from django.shortcuts import render, HttpResponse, redirect
from Main.models import Contact
# from home.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

OTP = get_random_string(4, allowed_chars='0123456789')
OTP1 = get_random_string(4, allowed_chars='0123456789')
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        User = authenticate(username=username,password=password)
        if User is not None:
            print(User)
            login(request, User)
            send_mail(
    "Logged In!",
    "Welcome "+request.user.first_name+",You Are Successfully Logged In to Your CareLink Account.",
    "lucknowbankof4@gmail.com",
    [request.user.email],
    fail_silently=False,
)
            return redirect("/panel")
        else:
            return render(request, 'panel.html')
    return render(request, 'login1.html')
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        username = request.POST.get('username')
        qualification = request.POST.get('qualification')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        CustID = request.POST.get('CustID')
        password = request.POST.get('password')
        contact=Contact(name=name, specialization=specialization, username=username, qualification=qualification, phone=phone, address=address, experience=experience, CustID=CustID, password=password)
        contact.save()
        # profile=Profile(balance='0')
        # profile.save()
        user = User.objects.create_user(username=username, email=CustID, password=password)
        user.first_name=name
        user.save()
        send_mail(
    "Congratulations!",
    "Welcome "+name+", Your Details has been successfully registered with us.Your CareLink Account has been successfully openned.Your Username (Customer ID) is"+username+" & Your Password is"+password,
    "lucknowbankof4@gmail.com",
    [CustID],
    fail_silently=False,
)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # profile_form.save()
        return redirect("/login1")
    return render(request, 'signup.html')
def profile(request):
    return render(request, 'profile.html')
def panel(request):
    if request.user.is_anonymous:
        return redirect("/index")
    context={
        "name":"User",
    }
    return render(request, 'panel.html', context)

# Create your views here.

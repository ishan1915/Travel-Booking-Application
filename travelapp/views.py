from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import *
from .forms import *
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
# Create your views here.
def loginview(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            messages.success(request, "Account created successfully!")
            return redirect("dashboard")  # redirect to your dashboard
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})

def dashboard_view(request):
    try:
        profile=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request,'dashboard.html',{'profile':profile})


def profile_edit(request):
    profile=get_object_or_404(Profile,user=request.user)
    if request.method=='POST':
        form=ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form=ProfileForm(instance=profile)
    return render(request, "edit_profile.html", {"form": form})



def create_booking(request):
    user = request.user
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  
            booking.user = user                 
            booking.total_price = (
                booking.number_of_seats * booking.travel_option.price
            )  # auto calculate
            booking.save()
            return redirect('dashboard')
    else:
        form = BookingForm()  
    return render(request, "booking.html", {"form": form})




 
def booking_history(request):
    user = request.user

    
    travel_type = request.GET.get("type")
    source = request.GET.get("source")
    destination = request.GET.get("destination")
    travel_date = request.GET.get("date")

    
    bookings = Booking.objects.filter(user=user).select_related("travel_option")

    
    if travel_type:
        bookings = bookings.filter(travel_option__type=travel_type)
    if source:
        bookings = bookings.filter(travel_option__source__icontains=source)
    if destination:
        bookings = bookings.filter(travel_option__destination__icontains=destination)
    if travel_date:
        bookings = bookings.filter(travel_option__date_time__date=travel_date)

    
    travel_types = TravelOption.objects.values_list("type", flat=True).distinct()
    sources = TravelOption.objects.values_list("source", flat=True).distinct()
    destinations = TravelOption.objects.values_list("destination", flat=True).distinct()

    return render(request, "booking_history.html", {
        "bookings": bookings,
        "travel_types": travel_types,
        "sources": sources,
        "destinations": destinations,
        "selected_type": travel_type,
        "selected_source": source,
        "selected_destination": destination,
        "selected_date": travel_date,
    })



def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    if booking.status != "Cancelled":
        booking.status = "Cancelled"
        booking.save()
    return redirect("booking_history")

#api views#############################################################################
@api_view(['POST'])
def login_apiview(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        serializer=UserSerializer(user)
        return Response({'msg':'login success','user':serializer.data},status=200)
    return Response(serializer.errors)


@api_view(['GET'])
def booking_all(request):
    booking=Booking.objects.all()
    serializers=BookingGetSerializer(booking,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def booking_detail(request):
    booking=Booking.objects.filter(user=request.user)
    serializer=BookingSerializer(booking,many=True)
    return Response(serializer.data)



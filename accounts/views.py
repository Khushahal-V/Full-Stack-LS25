from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Profile


# Register View
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Simulate verification
            user.save()
            return redirect('verify', token=user.profile.verification_token)

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import get_object_or_404
# Simulated Email Verification View
def verify_view(request, token):
    profile = get_object_or_404(Profile, verification_token=token)
    profile.is_verified = True
    profile.user.is_active = True
    profile.user.save()
    profile.save()
    messages.success(request, "Account Verified Successfully ✅")
    return redirect('login')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Account not verified.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View (Protected)
@login_required
def dashboard_view(request):
    profile = request.user.profile  # fetch profile using OneToOne relation
    return render(request, 'dashboard.html', {'profile': profile})


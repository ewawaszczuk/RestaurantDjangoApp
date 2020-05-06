from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import authenticate, login

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'User/register.html', {'form': form})

@login_required(login_url='/login/')
def profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    ctx = {'my_user_profile': my_user_profile}
    return render(request, 'User/profile.html', ctx)

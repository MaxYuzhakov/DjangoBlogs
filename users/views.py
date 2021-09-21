from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'({username}, you account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user_update_form = UserProfileUpdateForm()
    context = {
        'user_update_form': user_update_form,
    }
    return render(request, 'users/profile.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Job 

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login') #mapping
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form': form})


@login_required #decorator #adds functionality to profile #https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user) #populate form with existing info
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user) #populate form with existing info
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
#DISPLAYING LIST OF JOBS, replicating lines 36-38 above   
    context = {
        'jobs': Job.objects.all()
    }
    
    return render(request, 'users/profile.html', context)

    
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms.profile_form import ProfileForm
from django.contrib.auth.decorators import login_required
from user.models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print(request.FILES)
        form = ProfileForm(instance=profile, data=request.POST)
        print(request.FILES)
        if form.is_valid():
            print(request.FILES)
            profile = form.save(commit=False)
            print(request.FILES)
            profile.user = request.user
            print(request.FILES)
            profile.save()
            print(request.FILES)
            return redirect('profile')
            print(request.FILES)
        else:
            print(form.errors)
            print('no')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile, initial={'user': request.user})
    })


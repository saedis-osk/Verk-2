from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms.profile_form import ProfileForm
from django.contrib.auth.decorators import login_required
from user.models import Profile
import time
from PIL import Image

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

from PIL import Image

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            # Resize and save profile image
            if profile.profile_image:
                image = Image.open(profile.profile_image.path)
                output_size = (480, 480)
                image.thumbnail(output_size)
                image.save(profile.profile_image.path)

            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, initial={'user': request.user})
    return render(request, 'user/profile.html', {'form': form})

from django.forms import ModelForm, widgets, ClearableFileInput
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'user': widgets.HiddenInput()
        }
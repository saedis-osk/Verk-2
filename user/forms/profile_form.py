from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'image': widgets.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
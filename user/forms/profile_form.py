from django.forms import ModelForm, widgets, FileInput
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id']
        widgets = {
            'profile_image': widgets.FileInput(attrs={'class': 'image_selection_box'}),
            'name': widgets.TextInput(attrs={'class': 'text_box'}),
            'user': widgets.HiddenInput()
        }
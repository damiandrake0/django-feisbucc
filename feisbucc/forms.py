from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post,Profile

class SignupForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'}))

    class Meta:
        model = User 
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image_post','caption']

        # widgets = {
        #     'image_post':forms.FileInput(),
        #     'caption':forms.TextInput(attrs={'placeholder':'aggiungi una descrizione...'})
        # }

class EditProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','fullname','bio','mail']
        
        widgets = {
            'profile_pic':forms.FileInput(attrs={'class':'upload-btn'}),
            'fullname':forms.TextInput(attrs={'placeholder':'aggiungi il tuo nome'}),
            'bio':forms.TextInput(attrs={'placeholder':'aggiungi una descrizione...'}),
            'mail':forms.EmailInput(attrs={'placeholder':'aggiungi una mail'})
        }

    



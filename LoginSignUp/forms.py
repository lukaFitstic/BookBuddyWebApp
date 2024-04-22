from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(required = True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if User.objects.filter(email=user.username).exists():
            raise forms.ValidationError("Username is not unique")
        if commit:
            user.save()
            return user




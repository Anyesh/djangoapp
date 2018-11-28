from django import forms
from django.contrib.auth import authenticate, login, get_user_model

user = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Username', 'class':'form-control'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('username or password is incorrect.')

            if not user.check_password(password):
                raise forms.ValidationError('username or password is incorrect.')

            if not user.is_active:
                raise forms.ValidationError('user is inactive.')
        else:
            raise forms.ValidationError('username and password is required.')

        return super(UserLoginForm, self).clean(*args, **kwargs)

from django.forms import ModelForm
from apps.user_info.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "username",
            "email",
            Row(
                Column(
                    Field("password1", css_class="form-control"),
                    css_class="col-md-6",
                ),
                Column(
                    Field("password2", css_class="form-control"),
                    css_class="col-md-6",
                ),
                css_class="row",
            ),
        )

    # Backend validation (password match)
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return password2

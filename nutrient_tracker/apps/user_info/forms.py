"""Form for user registration."""

from typing import ClassVar

from apps.user_info.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from apps.user_info.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import BaseInput, Field, Layout, Row, Submit


class UserRegisterForm(UserCreationForm):
    """Base form for user registration."""

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model: ClassVar[object] = User
        fields: ClassVar[list] = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        """Initialize the form."""
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
    def clean_password2(self) -> str:
        """Validate that the two password entries match."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Passwords do not match!"
            raise forms.ValidationError(msg)
        return password2


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "contactform"
        self.helper.form_method = "post"
        self.helper.form_class = "mt-5"

        self.helper.layout = Layout(
            "name",
            "email",
            "message",
            Submit("submit", "Submit", css_class="btn-default"),
        )

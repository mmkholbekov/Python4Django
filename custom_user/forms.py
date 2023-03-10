from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VIP = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIP, "VIP"),
    (CLIENT, "CLIENT")
)

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
)

ASIA = 1
EUROPE = 2
AMERICA = 3
AFRICA = 4


REGION_TYPE = (
    (ASIA, "ASIA"),
    (EUROPE, "EUROPE"),
    (AMERICA, "AMERICA"),
    (AFRICA, "AFRICA"),

)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    region = forms.ChoiceField(choices=REGION_TYPE, required=True)
    country = forms.CharField(required=True)
    city = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender",
            "region",
            "country",
            "city",
            "address",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# core/forms.py
from django import forms
from .models import Student

class RegistrationForm(forms.ModelForm):
    """
    Form for user signup. Includes a password confirmation field.
    """
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = Student
        fields = [
            'full_name', 'email', 'password', 'password_confirm',
            'height_cm', 'weight_kg', 'age', 'level',
            'frequency_per_week', 'objective'
        ]

    def clean(self):
        cleaned = super().clean()
        pw = cleaned.get("password")
        pw2 = cleaned.get("password_confirm")
        # simple validation: passwords must match
        if pw and pw2 and pw != pw2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned

class LoginForm(forms.Form):
    """
    Minimal login form -- uses email + password for prototype.
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


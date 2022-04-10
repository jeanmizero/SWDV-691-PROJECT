from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

# Create Signup form class
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=300, help_text='eg. youremail@gmail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
        
# Create Contact form class
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50, required=True)
    name = forms.CharField(max_length=20, required=True)
    from_email = forms.EmailField(max_length=50, required=True)
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
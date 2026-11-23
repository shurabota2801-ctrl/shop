from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomerUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'email', 'password1', 'password2')

class AuthUserForm(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password')
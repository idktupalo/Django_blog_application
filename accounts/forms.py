from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model() # Get CustomUser from AUTH_USER_MODEL in settings.py
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # Get CustomUser from AUTH_USER_MODEL in settings.py
        fields = ('email', 'username')
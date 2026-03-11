from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUsercreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email") 
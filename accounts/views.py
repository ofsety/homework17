from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUsercreationForm

class SignUpView(CreateView):
    form_class = CustomUsercreationForm
    success_url = reverse_lazy("login")
    template_name = "acoounts/signup.html"
    
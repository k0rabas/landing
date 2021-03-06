from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "timestamp", "updated"]
    form = SignUpForm
#     class Meta:
#         model = SignUp

admin.site.register(SignUp, SignUpAdmin)
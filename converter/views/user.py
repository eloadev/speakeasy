from allauth.account.views import SignupView, LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from converter.forms.user import UserCreationForm
from converter.helpers.user import is_authenticated, is_admin
from converter.models import User


@user_passes_test(is_authenticated)
@user_passes_test(is_admin)
def create_user(request):
    if getattr(request.user, 'role', '') != User.Role.ADMIN:
        return HttpResponseForbidden("You don't have permission to access this page.")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', {'form': form})


class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

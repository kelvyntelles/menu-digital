from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.contrib import messages
from django.views.generic import View


def login_view(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Usuário ou senha inválidos."

    return render(request, 'painel/autenticacao/login.html', {
        'error': error_message
    })


class AlterarSenhaView(PasswordChangeView):
    template_name = "painel/autenticacao/alterar_senha_form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        messages.success(self.request, "Senha alterada com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = f"Usuário: {self.request.user.username}"
        return context

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        return render(request, "painel/autenticacao/logout.html")

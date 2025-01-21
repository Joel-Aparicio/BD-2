from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from BD2_Trabalhofinal.App.models import Utilizador

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print(f"Tentando autenticar o usuário com o email: {email}")
        try:
            user = Utilizador.objects.get(email=email)
            print(f"Usuário encontrado: {user.nome}")
            if check_password(password, user.palavra_passe):
                print("Senha válida, autenticando usuário")
                return user
            else:
                print("Senha inválida")
                return None
        except Utilizador.DoesNotExist:
            print("Usuário não encontrado")
            return None

    def get_user(self, user_id):
        try:
            return Utilizador.objects.get(pk=user_id)
        except Utilizador.DoesNotExist:
            return None

from django.apps import AppConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BD2_Trabalhofinal.App'  
    
    def ready(self):
        import BD2_Trabalhofinal.App.signals  # Importa os sinais
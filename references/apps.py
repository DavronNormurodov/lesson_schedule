from django.apps import AppConfig


class ReferencesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'references'

    def ready(self):
        import references.signals as reference_signals

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Course Platform Core'

    def ready(self):
        # Import signals or perform other startup tasks here
        pass


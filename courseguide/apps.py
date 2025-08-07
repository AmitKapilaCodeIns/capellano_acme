from django.apps import AppConfig


class CourseguideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courseguide'

    def ready(self):
        # Import signals or other initialization code here if needed
        import courseguide.signals  # Ensure signals are imported

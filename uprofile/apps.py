from django.apps import AppConfig


class UprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uprofile'

    # def ready(self):
    #     import profile.signals

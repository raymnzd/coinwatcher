from django.apps import AppConfig


class DisplayConfig(AppConfig):
    name = 'display'

    def ready(self):
        import display.signals

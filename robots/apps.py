from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = 'robots'
    verbose_name = 'Роботы'

    def ready(self):
        import api.robots.signals

from django.apps import AppConfig


class MoneyrelationsConfig(AppConfig):
    name = 'MoneyRelations'

    def ready(self):
        from django.conf import settings
        print(settings.TEMPLATES[0]["DIRS"])
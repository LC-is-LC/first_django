from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'Users'

    # the signals.py is imported, so that everything that happens there will occur after each user is created
    def ready(self):
        import Users.signals
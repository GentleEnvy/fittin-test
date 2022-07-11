from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.products'

    def ready(self):
        super().ready()
        __import__(f'{self.name}.signals')

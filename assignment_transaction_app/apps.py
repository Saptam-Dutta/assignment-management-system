from django.apps import AppConfig


class AssignmentTransactionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assignment_transaction_app'

    def ready(self):
        import assignment_transaction_app.signals

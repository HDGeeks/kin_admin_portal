from django.apps import AppConfig


class PodcastConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'podcast'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        # Explicitly connect a signal handler.
        # post_save.connect(signals.update_document)
        # post_delete.connect(signals.delete_document)

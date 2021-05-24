from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProblemConfig(AppConfig):
    name = 'problem'
    verbose_name = _('profiles')

    def ready(self):
        import problem.signals

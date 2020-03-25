from django.conf import settings
from psu_base.services import utility_service
from psu_base.classes.Log import Log

log = Log()


class DynamicRole:
    prod = None
    non_prod = None

    def __init__(self):
        self.prod = utility_service.is_production()
        self.non_prod = not self.prod

    def plus(self, additional):
        if type(additional) is str:
            ll = utility_service.csv_to_list(additional)
        elif type(additional) is list:
            ll = additional
        else:
            ll = []

        return ll if ll else []

    def power_user(self, plus=None):
        """
        The lowest-level of increased authority on a site.
        Gets access to base features like viewing audit logs or editing infotext
        """
        # This will be the same for prod and non-prod (at least for now)
        if self.prod:
            pass

        return ['admin', 'developer', 'oit-es-manager'] + self.plus(plus)

    def super_user(self, plus=None):
        """
        An increased level of authority.
        Perhaps features not suitable for non-technical users, or features that affect site functions.
        """
        if self.prod:
            return ['oit-es-manager'] + self.plus(plus)
        else:
            return ['developer', 'oit-es-manager'] + self.plus(plus)

    def security_officer(self, plus=None):
        """
        Allows access to monitor security features (i.e. review XSS attempts), and to modify user permissions
        """
        if self.prod:
            return ['authorize', 'oit-es-manager'] + self.plus(plus)
        else:
            return ['authorize', 'developer', 'oit-es-manager'] + self.plus(plus)

    def impersonator(self, plus=None):
        """
        Allows impersonation
        """
        if self.prod:
            return ['oit-es-manager'] + self.plus(plus)
        else:
            return ['admin', 'impersonate', 'developer', 'oit-es-manager'] + self.plus(plus)

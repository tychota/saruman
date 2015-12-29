__all__ = ['FirewallGenericError']


class FirewallGenericError(Exception):
    pass


class FirewallNotAllowedError(FirewallGenericError):
    pass

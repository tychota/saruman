# -*- coding: utf-8 -*-

__all__ = ['FirewallGenericError']


class FirewallGenericError(Exception):
    pass


class FirewallNotAllowedError(FirewallGenericError):
    pass

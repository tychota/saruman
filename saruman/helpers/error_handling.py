import contextlib
import logging

from plumbum.commands.processes import ProcessExecutionError, CommandNotFound, ProcessTimedOut
from celery.exceptions import (SecurityError, Ignore, QueueNotFound, WorkerShutdown, WorkerTerminate,
                               ImproperlyConfigured, NotRegistered, AlreadyRegistered,
                               MaxRetriesExceededError, Retry,
                               TaskRevokedError, NotConfigured, AlwaysEagerIgnored,
                               InvalidTaskError, ChordError, CPendingDeprecationWarning,
                               CDeprecationWarning, FixupWarning, DuplicateNodenameWarning,
                               SoftTimeLimitExceeded, TimeLimitExceeded, WorkerLostError,
                               Terminated)
from saruman.helpers.exceptions import FirewallGenericError

__all__ = ['error_handling']

WARNING = (Ignore, AlreadyRegistered, TimeoutError, CPendingDeprecationWarning,
           CDeprecationWarning, FixupWarning, DuplicateNodenameWarning,
           SoftTimeLimitExceeded, Retry)
HANDLED_ERROR = ()
UNHANDLED_ERROR = (ProcessTimedOut, WorkerShutdown, WorkerTerminate, ImproperlyConfigured, NotRegistered,
                   MaxRetriesExceededError, TaskRevokedError, NotConfigured, AlwaysEagerIgnored, InvalidTaskError,
                   ChordError, FirewallGenericError, TimeLimitExceeded, WorkerLostError, Terminated)
CRITICAL = (ProcessExecutionError, CommandNotFound, SecurityError, QueueNotFound)


@contextlib.contextmanager
def error_handling(logger):
    try:
        assert isinstance(logger, logging.Logger)
        try:
            yield
        except WARNING as e:
            logger.warning(e)
        except UNHANDLED_ERROR as e:
            logger.error(e)
            raise
        except HANDLED_ERROR as e:
            logger.error(e)
        except CRITICAL as e:
            logger.critical(e)
    except Exception as e:
        print(e)

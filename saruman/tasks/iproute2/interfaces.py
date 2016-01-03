from celery import Task
from celery.utils.log import get_task_logger

# noinspection PyUnresolvedReferences
from plumbum.cmd import lsmod, modprobe

from saruman.helpers.error_handling import error_handling
from saruman.helpers.exceptions import FirewallNotAllowedError

__all__ = ['check']

logger = get_task_logger(__name__)


class Bridge(Task):
    name = 'kernel.modules.check'

    @error_handling(logger)
    def run(self, module_name, **kwargs):
        logger.info("Check pour voir si le module `{}` du kernel est activé".format(module_name))
        logger.debug("Execution de lsmod")
        mod = lsmod()
        return module_name in mod

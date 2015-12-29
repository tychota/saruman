from celery.utils.log import get_task_logger
from celery import Task, states
from celery.exceptions import Ignore
# noinspection PyUnresolvedReferences
from plumbum.cmd import lsmod, modprobe


from firewall.app.queue import queue

from firewall.helpers.exceptions.plumbum import ProcessExecutionError
from firewall.helpers.exceptions.firewall import FirewallGenericError, FirewallNotAllowedError

__all__ = ['check']

logger = get_task_logger(__name__)

allowed_mod = ['dummy']


class Check(Task):
    name = 'kernel.modules.check'

    def run(self, module_name, **kwargs):
        logger.info("Check pour voir si le module `{}` du kernel est activé".format(module_name))
        try:
            if module_name not in allowed_mod:
                raise FirewallNotAllowedError("Le module `{}` du kernel n'est pas whitelisté".format(module_name))
            logger.debug("Execution de lsmod")
            mod = lsmod()
            return module_name in mod
        except (ProcessExecutionError, FirewallGenericError) as e:
            logger.error(e)
        except Exception as e:
            logger.exception(e)


class Add(Task):
    name = 'kernel.modules.add'

    def run(self, module_name, module_args, **kwargs):
        logger.info("Activation du module `{}` du kernel".format(module_name))
        try:
            if module_name not in allowed_mod:
                raise FirewallNotAllowedError("Le module `{}` du kernel n'est pas whitelisté".format(module_name))
            logger.debug("Execution de modprobe")
            if module_args is not None:
                mod = modprobe[module_name, module_args]()
            else:
                mod = modprobe[module_name]()
            actif = mod
            logger.info("Le module `{}` du kernel est {}".format(module_name, "activé" if actif else "désactivé"))
            return actif
        except (ProcessExecutionError, FirewallGenericError) as e:
            logger.error(e)
        except Exception as e:
            logger.exception(e)

if __name__ == '__main__':
    Check().delay("test")

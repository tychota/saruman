from celery import Task
from celery.utils.log import get_task_logger

# noinspection PyUnresolvedReferences
from plumbum.cmd import lsmod, modprobe

from saruman.helpers.error_handling import error_handling
from saruman.helpers.exceptions import FirewallNotAllowedError

__all__ = ['Check', 'Add', 'AddWithArgs', 'Remove']

logger = get_task_logger(__name__)

allowed_mod = ['dummy']


class Check(Task):
    """
    Tache de vérification de l'activation d'un module dans le kernel

    Vérifie si le module `module_name` est activé dans le kernel.
    Se réfère à une liste des modules autorisés (ainsi, l'utilisateur ne peut pas
    supprimer le module du filesystem par exemple).
    La tache tourne dans un context (:py:func:error_handling) qui gère les erreurs

    """
    name = 'kernel.modules.check'

    def run(self, module_name):
        """
        :param  str module_name: le nom du module à checker
        :return: oui si le module est activé, non sinon
        :rtype: bool
        """
        with error_handling(logger):
            logger.info("Check pour voir si le module `{}` du kernel est activé".format(module_name))
            if module_name not in allowed_mod:
                raise FirewallNotAllowedError("Le module `{}` du kernel n'est pas whitelisté".format(module_name))
            logger.debug("Execution de lsmod")
            mod = lsmod()
            return module_name in mod


class Add(Task):
    """
    Tache de vérification de l'activation d'un module dans le kernel

    Vérifie si le module `module_name` est activé dans le kernel.
    Se réfère à une liste des modules autorisés (ainsi, l'utilisateur ne peut pas
    supprimer le module du filesystem par exemple).
    La tache tourne dans un context (:py:func:error_handling) qui gère les erreurs
    """
    name = 'kernel.modules.add'

    def run(self, module_name):
        """
        :param str module_name: le nom du module à checker
        """
        with error_handling(logger):
            logger.info("Activation du module `{}` du kernel".format(module_name))
            if module_name not in allowed_mod:
                raise FirewallNotAllowedError("Le module `{}` du kernel n'est pas whitelisté".format(module_name))
            logger.debug("Execution de modprobe")
            result = modprobe[module_name]()
            logger.info("Le module `{}` du kernel est {}".format(module_name, "activé" if result else "désactivé"))


class AddWithArgs(Task):
    """
    Tache de vérification de l'activation d'un module dans le kernel

    Vérifie si le module `module_name` est activé dans le kernel.
    Se réfère à une liste des modules autorisés (ainsi, l'utilisateur ne peut pas
    supprimer le module du filesystem par exemple).
    La tache tourne dans un context (:py:func:error_handling) qui gère les erreurs
    """
    name = 'kernel.modules.addWithArgs'

    def run(self, module_name, module_args):
        """
        :param str module_name: le nom du module à checker
        :param dict module_args: un dictionnaire d'arguments
        """
        with error_handling(logger):
            logger.info("Activation du module `{}` du kernel".format(module_name))
            if module_name not in allowed_mod:
                raise FirewallNotAllowedError("Le module `{}` du kernel n'est pas whitelisté".format(module_name))
            logger.debug("Execution de modprobe")
            arguments = ['{}={}'.format(k, v) for k, v in module_args.items()]
            arguments = [module_name].extend(arguments)
            result = modprobe(arguments)
            logger.info("Le module `{}` du kernel est {}".format(module_name, "activé" if result else "désactivé"))


class Remove(Task):
    name = 'kernel.modules.remove'

    def run(self, module_name):
        with error_handling(logger):
            logger.info("Désactivation du module `{}` du kernel".format(module_name))
            if module_name not in allowed_mod:
                raise FirewallNotAllowedError("Le module `{}` du kernel n'est pas whitelisté".format(module_name))
            logger.debug("Execution de modprobe")
            result = modprobe["-r", module_name]()
            logger.info("Le module `{}` du kernel est {}".format(module_name, "activé" if result else "désactivé"))

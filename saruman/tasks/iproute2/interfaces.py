# -*- coding: utf-8 -*-

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
    def run(self, bridge_name, interface_name):
        logger.info("Création d'un nouveau bridge `{}`".format(bridge_name))
        logger.debug("Execution de ip")

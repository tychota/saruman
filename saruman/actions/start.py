# -*- coding: utf-8 -*-
import logging

from saruman.app.queue import queue

import saruman.tasks.kernel.modprobe

__all__ = ['check']

logger = logging.getLogger(__name__)


def start_all():
    logger.warn("Chargement du module kernel dummy")
    log_pref = "Module Kernel `dummy` - "
    logger.info(log_pref + 'Check si le module est chargé')
    dummy_check_result = saruman.tasks.kernel.modprobe.Check().delay('dummy')
    logger.info(log_pref + 'La commande de check a retourné: {}'.format(dummy_check_result.get()))
    logger.info(log_pref + 'Le module {} activé'.format("est" if dummy_check_result.get() else "n'est pas"))
    if not dummy_check_result.get():
        logger.info(log_pref + 'Activation du module')
        dummy_active_result = saruman.tasks.kernel.modprobe.Add().delay('dummy', '')
        if dummy_active_result.get() is not None:
            logger.info(log_pref + 'La commande a retourné: `{}`'.format(dummy_active_result.get()))
        else:
            logger.error(log_pref + 'La commande a echoué ! Regarde les logs workers')
    logger.warn("Chargement du module kernel bridge")
    log_pref = "Module Kernel `bridge` - "
    logger.info(log_pref + 'Check si le module est chargé')
    bridge_check_result = saruman.tasks.kernel.modprobe.Check().delay('bridge')
    logger.info(log_pref + 'La commande de check a retourné: {}'.format(bridge_check_result.get()))
    logger.info(log_pref + 'Le module {} activé'.format("est" if bridge_check_result.get() else "n'est pas"))
    if not bridge_check_result.get():
        logger.info(log_pref + 'Activation du module')
        bridge_active_result = saruman.tasks.kernel.modprobe.Add().delay('bridge', '')
        if bridge_active_result.get() is not None:
            logger.info(log_pref + 'La commande a retourné: `{}`'.format(bridge_active_result.get()))
        else:
            logger.error(log_pref + 'La commande a echoué ! Regarde les logs workers')

if __name__ == '__main__':
    start_all()

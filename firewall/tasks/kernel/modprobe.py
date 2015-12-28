from celery.utils.log import get_task_logger

from firewall.app.queue import queue
from firewall.helpers.command import modprobe
from firewall.helpers.exceptions import ProcessExecutionError

logger = get_task_logger(__name__)


@queue.task
def check_and_add_module(module_name, **kwargs):
    logger.error("Tente d'executer modprobe avec le paramètre {}")
    try:
        mod = modprobe()
    except ProcessExecutionError:
        logger.critical("Impossible d'excuter modprobe")


if __name__ == '__main__':
    check_and_add_module("test")

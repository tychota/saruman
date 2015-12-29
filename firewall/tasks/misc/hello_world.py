from celery.utils.log import get_task_logger

from firewall.app.queue import queue

logger = get_task_logger(__name__)


@queue.task(name='misc.hello')
def hello(x):
    logger.info("It is a ...")
    logger.info(x)

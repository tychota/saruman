from celery.utils.log import get_task_logger

from firewall.app import queue

logger = get_task_logger(__name__)


@queue.task
def test(x):
    logger.info("It is a ...")
    logger.info(x)

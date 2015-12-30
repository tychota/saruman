def get_celery_worker_status():
    error_key = "ERROR"
    try:
        # noinspection PyUnresolvedReferences
        from celery.task.control import inspect
        inspection = inspect()
        d = inspection.stats()
        if not d:
            d = {error_key: 'No running Celery workers were found.'}
    except IOError as e:
        from errno import errorcode
        msg = "Error connecting to the backend: " + str(e)
        if len(e.args) > 0 and errorcode.get(e.args[0]) == 'ECONNREFUSED':
            msg += ' Check that the RabbitMQ server is running.'
        d = {error_key: msg}
    except ImportError as e:
        d = {error_key: str(e)}
    return d

if __name__ == '__main__':
    get_celery_worker_status()

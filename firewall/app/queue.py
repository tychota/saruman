import celery

queue = celery.Celery("firewall",
                      backend='amqp://guest@localhost//',
                      broker='amqp://guest@localhost//',
                      include=["tasks"])

queue.config_from_object("conf.celery")

if __name__ == '__main__':
    queue.start(argv=['app.queue', 'worker', '-l', 'info'])

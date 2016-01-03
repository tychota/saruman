import celery

queue = celery.Celery("saruman",
                      backend='amqp://guest@localhost//',
                      broker='amqp://guest@localhost//',
                      include=[
                          "saruman.tasks",
                          "saruman.tasks.kernel",
                          "saruman.tasks.firewall",
                      ])

queue.config_from_object("saruman.conf.celery")

if __name__ == '__main__':
    pass

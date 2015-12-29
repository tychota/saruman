import celery

queue = celery.Celery("firewall",
                      backend='amqp://guest@localhost//',
                      broker='amqp://guest@localhost//',
                      include=[
                          "firewall.tasks",
                          "firewall.tasks.kernel",
                          "firewall.tasks.firewall",
                      ])

queue.config_from_object("firewall.conf.celery")

if __name__ == '__main__':
    pass

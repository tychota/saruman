Saruman
=======

Saruman: a logic, configuration based, distribuable firewall.

Saruman is a extended firewall (meaning firewall + dns + dhcp +intruision detection + reverse proxy)
build by a former `Iresam <https://www.iresam.org>`_.
It targets I-Resam need's first but should be enough flexible to be used elsewhere.

It still unstable and yet brings not that much.
Try at your own risks.

Most important Urls
-------------------

- The full documentation is at `saruman.readthedocs.org <https://readthedocs.org/projects/saruman/>`_

- We are `on Pypi <https://pypi.python.org/pypi/saruman>`_ so we're only
  an ``pip install saruman`` away from installation on your computer.

- The code is at `github.com/tychota/saruman
  <https://github.com/tychota/saruman>`_.

And... we're automatically being tested by Travis and Landscape:

Technologies used
-----------------

- Saruman **does require** Python 3, and if possible the newest version (**Python3.5** for now)

- It **does require** an Celery broker : take **RabbitMQ**, it is good, fast and reliable.

- It **does only works** on a recent linux machine : it requires **nftables** and **iproute2** so a linux 4+ kernel
  would be a necessity.

Available commands
------------------

Saruman gives you three commands to manage the worker and one to run your firewall.
Worker's commands must be run in root since they manage main parts of your system.
Firewall's one doesn't need this.
The commands are:

- **saruman workers enable**: start the celery workers on the machine.

- **saruman workers disable**: start the celery workers on the machine.

- **saruman workers reload**: restart the celery workers on the machine.

- **saruman firewall start**: start the firewall

AMQP json-rpc api
-----------------

Still infant
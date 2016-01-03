Information for developers of saruman
=====================================

Running tests
-------------

We like to use Virtual env to get a simple environment and to use pytest to test.
When you are in the root folder of your *saruman* checkout, do this::

  $ virtualenv ~/venv/saruman --python=`which python3.5`  # Or a different python version.
  $ source ~/venv/firewall/bin/activate
  $ python setup.py test


Python versions
---------------

The tests currently pass on python 3.4 and 3.5. Travis continuous
integration tests 3.4 and 3.5 for us automatically.


Necessary programs
------------------

To run the firewall and test, you need to have an AMQP broker !
On ubuntu::

  $ sudo apt-get install rabbitmq

Assumptions
===========

*Saruman* originated at `Iresam <https://iresam.org>`_ so there
are some assumptions build-in that might or might not fit you but I'm pretty
sure it'll probably fit :-)

- In our case, *saruman* is run on a VM cluster so we have different VM handling different stuff
  For instance one for the netfilter firewall and router, one for dhcp, one for reverse proxy,
  one for admin site, one for AMQP broker so you have to tag the tasks you create so *saruman*
  could know which VM has to handle what.


That's just the style we started with.  Pretty clear and useful.

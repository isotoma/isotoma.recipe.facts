Introduction
============

This package provides information about the host you are running buildout on.


Exposed Parameters
==================

hostname
    The hostname of the machine buildout is running on, as returned by ``socket.gethostname()``
fqdn
    The fully qualified domain of the machine buildout is running on, as return by ``socket.getfqdn()``.
    If no fqdn is available, this will be the same as hostname.
interface.X.address
    The IP address of the network interface ``X``.


Using facts
===========

This example uses the missingbits echo recipe to print information about the current machine::

    [buildout]
    parts = echo

    [facts]
    recipe = isotoma.recipe.facts

    [echo]
    recipe = missingbits:echo
    echo =
        The hostname is ${facts:hostname}
        The fdqn is ${facts:fdqn}
        The main IP address is ${facts:interface.eth0.address}


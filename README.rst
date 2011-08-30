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
user.name
    The name of the account running buildout
user.uid
    The uid running buildout. Numerical.
user.gid
    The gid running buildout. Numerical.
user.home
    The home directory of the user running buildout
vcs.type
    The type of checkout that buildout is being run from. Supports Git or SVN, otherwise will be 'unknown'.
vcs.branch
    The branch or that that buildout is being run from. Will be 'unknown' for unsupported VCS.


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
        The VCS type is ${facts:vcs.type} and branch is ${facts:vcs.branch}
        The user is ${facts:user.name} and their home dir is ${facts:user.home}


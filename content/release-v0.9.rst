Release of wharfee v0.9
#######################

:date: 2016-7-14
:tags: python, wharfee, release
:category: blog
:author: Irina
:slug: wharfee-release-v0.9

`Wharfee`_ is a shell for Docker that can do autocompletion and syntax
highlighting, as well as some useful shortcuts.

It is now more stable than ever, thanks to newly added integration tests.

New features in this release:

* Added ``-f/--force`` flag to ``rm`` command.
* Added ``--detach-keys`` option to ``attach`` command.

Fixes and improvements:

* Fix exception in py3 when printing out ``pull`` output.
* Fix exception in py3 when printing out ``logs`` output.
* Fix exception in py2.6 when printing out ``rm`` output.
* Fix bug in ``rm --all`` shortcut, which did not really remove stopped containers.
* Fix bug in ``start``, which was not called unless interactive flag was set.
* Fix output of ``port`` command with no port mappings.
* Handle exception in ``inspect`` when argument is not a container or image name.
* ``run`` now uses pexpect to call external cli, because new version of docker-py was throwing "jack is incompatible with use of CloseNotifier in same ServeHTTP call".

.. _wharfee: http://wharfee.com

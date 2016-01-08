Release of wharfee v0.7
#######################

:date: 2016-1-7
:tags: python, wharfee, release
:category: Blog
:slug: wharfee-release-v0.7

`Wharfee`_ is a shell for Docker that can do autocompletion and syntax
highlighting, as well as some useful shortcuts.

What's new in 0.7:

* Added ``volume`` commands:

::

  volume create
  volume rm
  volume ls
  volume inspect

* Added ``--all`` shortcut option to ``rm`` and ``rmi`` commands.
* Internal fixes and updates, including update of `Python Prompt Toolkit`_ to 0.57.

.. _wharfee: http://wharfee.com
.. _request: https://github.com/j-bennet/wharfee/issues/89
.. _wikipedia: https://en.wikipedia.org/wiki/Stevedore
.. _`Python Prompt Toolkit`: http://github.com/jonathanslenders/python-prompt-toolkit

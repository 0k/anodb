=========================
anodb
=========================

.. image:: http://img.shields.io/pypi/v/anodb.svg?style=flat
   :target: https://pypi.python.org/pypi/anodb/
   :alt: Latest PyPI version

.. image:: http://img.shields.io/pypi/dm/anodb.svg?style=flat
   :target: https://pypi.python.org/pypi/anodb/
   :alt: Number of PyPI downloads

.. image:: http://img.shields.io/travis/0k/anodb/master.svg?style=flat
   :target: https://travis-ci.org/0k/anodb/
   :alt: Travis CI build status

.. image:: http://img.shields.io/coveralls/0k/anodb/master.svg?style=flat
   :target: https://coveralls.io/r/0k/anodb
   :alt: Test coverage



``anodb`` is a Python Command Line tool to help you anonymize an existing
database.


Maturity
========

This code is in alpha stage. It wasn't tested on Windows. API may change.
This is more a draft for an ongoing reflection.


Features
========

using ``anodb``:

- You can simply replace fields in your database, conditionally, with
  other values if needed.

- You can empty target tables

- And these actions can be saved in a YML file that would batch all
  these actions.

- All commands support ``--dry-run`` to see what is the SQL that would
  be executed.


Compatibility
=============

This code is python2 ready. It wasn't tested on windows.


Requirements
============

You need ``libpq-dev`` and ``libpython-dev`` package to install it, as
it required python ``psycopg2`` to access the database:

    apt-get install libpq-dev libpython-dev


Installation
============

You don't need to download the GIT version of the code as ``anodb`` is
available on the PyPI. So you should be able to run::

    pip install anodb

If you have downloaded the GIT sources, then you could add install
the current version via the traditional way::

    python setup.py install

And if you don't have the GIT sources but would like to get the latest
master or branch from github, you could also::

    pip install git+https://github.com/0k/anodb

Or even select a specific revision (branch/tag/commit)::

    pip install git+https://github.com/0k/anodb@master


Usage
=====


Database access
---------------

Before using ``anodb`` you should set up your environment for
password-less access to your target database. This can be done with
several different ways.

#. on the server side: using postgres ``pg_hba.conf`` to set password less
   access to some specified login (RECOMMENDED ONLY ON LOCAL SOCKET ACCESS)

#. on the client side, for system authentication: thanks to ``sudo``,
   setting a password-less working ``sudo`` access to a user having
   system authentication (typically ``sudo -u postgres``).

#. on the client side, using environment variables: setting
   ``PGUSER``, ``PGPASSWORD``, ``PGDATABASE``, ``PGHOST``,
   ``PGPORT``...

#. on the client side, using the ``~/.pgpass`` file...

To check the access is fully working you should simply test that
launching ``psql`` alone will connect you without errors to the
correct database.

In a unclear future, a few command line arguments could be added so
that you can provide directly a DSN or the necessary information to
choose and connect to any database.


Get help
--------

    anodb --help


Replace fields
--------------

     anodb replace fields --help


Clear Table
-----------

     anodb clear table --help


Script
------

    anodb script --help


Contributing
============

Any suggestion or issue is welcome. Push request are very welcome,
please check out the guidelines.


Push Request Guidelines
-----------------------

You can send any code. I'll look at it and will integrate it myself in
the code base and leave you as the author. This process can take time and
it'll take less time if you follow the following guidelines:

- check your code with PEP8 or pylint. Try to stick to 80 columns wide.
- separate your commits per smallest concern.
- each commit should pass the tests (to allow easy bisect)
- each functionality/bugfix commit should contain the code, tests,
  and doc.
- prior minor commit with typographic or code cosmetic changes are
  very welcome. These should be tagged in their commit summary with
  ``!minor``.
- the commit message should follow gitchangelog rules (check the git
  log to get examples)
- if the commit fixes an issue or finishes the implementation of a
  feature, please mention it in the summary.

If you have some questions about guidelines which is not answered here,
please check the current ``git log``, you might find previous commit that
would show you how to deal with your issue.


License
=======

Copyright (c) 2016 Valentin Lab.

Licensed under the `BSD License`_.

.. _BSD License: http://raw.github.com/0k/anodb/master/LICENSE

# -*- coding: utf-8 -*-

from . import common


class Command(common.DbCommand):
    """Check access

    Connects to database and check access

    Usage:
      %(std_usage)s
      %(surcmd)s [-q|--quiet] [--dry-run]

    Options:
      %(std_options)s
      --dry-run         Do nothing and print the SQL that would be executed.
      -q, --quiet        Suppress outputs.

    """

    def __call__(self, quiet=False, dry_run=False):
        query = "SELECT 1"
        if dry_run:
            print self.db.mogrify(query)
        else:
            self.db.execute(query)

        self._connection.commit()

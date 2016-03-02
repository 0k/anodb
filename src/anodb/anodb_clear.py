# -*- coding: utf-8 -*-

from . import common

from kids.cmd import cmd


class Command(common.DbCommand):
    """Clear objects (tables, fields)

    Will remove data from target database

    Usage:
      %(std_usage)s

    """

    @cmd
    def table(self, table, quiet=False, dry_run=False):
        """Clear Target Table in Target Database

        Remove all records from specified table without deleting it.

        Usage:
          %(std_usage)s
          %(surcmd)s TABLE [-q|--quiet] [--dry-run]

        Options:
          %(std_options)s
          --dry-run         Do nothing and print the SQL that would be executed.
          -q, --quiet        Suppress outputs.

        """

        query = "DELETE FROM %s" % table
        if dry_run:
            print self.db.mogrify(query)
        else:
            self.db.execute(query)

        self._connection.commit()

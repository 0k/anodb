# -*- coding: utf-8 -*-

from . import common

from kids.cmd import cmd, msg


class Command(common.DbCommand):
    """Clear objects (tables, fields)

    Will remove data from target database

    Usage:
      %(std_usage)s

    """

    def __init__(self, env=None):
        self.env = env or {}
        super(Command, self).__init__()

    @cmd
    def field(self, table, field, pattern, where="1=1", dry_run=False,
              quiet=False):
        """Clear Target Table in Target Database

        Remove all records from specified table without deleting it.

        Usage:
          %(std_usage)s
          %(surcmd)s TABLE FIELD PATTERN [-w|--where WHERE] [--dry-run]
              [-q|--quiet]

        Options:
          %(std_options)s
          TABLE             Target Table
          FIELD             Target Field in TABLE
          PATTERN           Replacement pattern, this is python code that gets
                            the full current record as environment. It'll be
                            evaluated for each record, and the result of the
                            evaluation will be used as the new value of the
                            field.
          -w,--where WHERE
                            Adds a where clause to the UPDATE command.
          --dry-run         Do nothing and print the SQL that would be executed.
          -q, --quiet        Suppress outputs.

        """
        self.db.execute("SELECT * FROM %(table)s WHERE %(where)s" % {
            "table": table,
            "where": ",".join(where) if isinstance(where, list) else where,
        })

        count = 0
        for record in self.db.fetchall():
            count += 1
            env = getattr(self, "env", {}).copy()
            env.update(record)
            value = eval(pattern, globals(), env)
            sql = ("UPDATE %(table)s SET %(field)s = %%s WHERE %(where)s" % {
                "table": table,
                "where": "id = %s" % (record["id"], ),
                "field": field,
            }) , (value, )
            if not quiet:
                msg.info("replacing field '%s' value %r with %r"
                         % (field, record[field], value))
            if dry_run:
                print self.db.mogrify(*sql)
            else:
                self.db.execute(*sql)
        if not quiet and not dry_run:
            msg.info("Replaced value of field %r in %d record(s)."
                     % (field, count))

        if not dry_run:
            self._connection.commit()

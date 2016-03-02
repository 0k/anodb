# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras

from kids.cache import cache
from kids.cmd import BaseCommand


class DbCommand(BaseCommand):

    @cache
    @property
    def _connection(self):
        try:
            return psycopg2.connect(dsn="")
        except (TypeError, psycopg2.OperationalError):
            raise SystemError(
                "Please set correct PG connection information in current shell "
                "environment. (ie: PGUSER, PGDATABASE, PGPASSWORD, PGHOST...)")

    @cache
    @property
    def db(self):
        return self._connection.cursor(
            cursor_factory=psycopg2.extras.DictCursor)


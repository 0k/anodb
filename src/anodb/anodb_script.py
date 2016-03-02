# -*- coding: utf-8 -*-

import yaml

from . import common
from . import anodb_replace
from . import anodb_clear

from kids.cmd import msg


class Command(common.DbCommand):
    """Script

    Load YML script and load it

    Usage:
      %(std_usage)s
      %(surcmd)s SCRIPT [--dry-run] [-q|--quiet]

        Options:
          %(std_options)s
          SCRIPT            YAML script name to load and execute
          --dry-run         Do nothing and print the SQL that would be executed.
          -q, --quiet        Suppress outputs.


    """

    def __call__(self, script, quiet=False, dry_run=False):
        s = yaml.load(file(script, 'r'))

        ##
        ## Environment
        ##
        env_code = s.get('env', '')

        env = {}
        if env_code:
            try:
                code = compile(env_code, '<env>', 'exec')
                exec(code, env)
            except SyntaxError as e:
                raise SyntaxError(
                    'Syntax error in provided env ('
                    'Line %i offset %i)' % (e.lineno, e.offset))
            env = dict((k, v) for k, v in env.items()
                       if k != "__builtins__")


        ##
        ## Actions
        ##

        actions = s.get('actions', '')
        if actions:
            for nb_action, action in enumerate(actions):
                for name, sub_actions in action.items():
                    if name == 'replace':
                        cmd = anodb_replace.Command(env=env)
                        for sub_action in sub_actions:
                            for subcmd, sub_actions2 in sub_action.items():
                                if subcmd == 'field':
                                    subcmd = getattr(cmd, subcmd)
                                    for params in sub_actions2:
                                        kwargs = {}
                                        for tablename, arguments in params.items():
                                            for label, value in arguments.items():
                                                if label.startswith('--'):
                                                    label = label[2:]
                                                    kwargs[label] = value
                                                    continue
                                                subcmd(tablename, label, value, dry_run=dry_run, quiet=quiet, **kwargs)
                                else:
                                    msg.die("Invalid subcommand %r for action %r." % (subcmd, name))
                    elif name == 'clear':
                        cmd = anodb_clear.Command()
                        for sub_action in sub_actions:
                            for subcmd, sub_actions2 in sub_action.items():
                                if subcmd == 'table':
                                    subcmd = getattr(cmd, subcmd)
                                    for tablename in sub_actions2:
                                        kwargs = {}
                                        subcmd(tablename, dry_run=dry_run, quiet=quiet, **kwargs)
                                else:
                                    msg.die("Invalid subcommand %r for action %r." % (subcmd, name))
                    else:
                        msg.die("Invalid action %r (action number %d)" % (name, nb_action + 1))

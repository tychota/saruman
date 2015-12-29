#!/usr/bin/env python3
from traceback import format_tb

import click
import pprint
import time
from colorlog import ColoredFormatter
import celery.bin.multi

from firewall.app.queue import queue
from firewall.actions.start import start_all

import logging
logger = logging.getLogger()
logger.setLevel(logging.WARN)

stream_handler = logging.StreamHandler()
formatter = ColoredFormatter(
        "%(log_color)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red',
        }
)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


__all__ = ['cli']


@click.group()
@click.help_option(help="Affiche ce message")
@click.version_option(version='1.0.0', help="Affiche la version")
def cli():
    pass


@cli.group(short_help="( enable | disable) Active ou desactive les workers")
@click.help_option(help="Affiche ce message")
def worker():
    pass


@worker.command(short_help="Active les workers", help="Affiche ce message")
@click.help_option(help="Affiche ce message")
@click.option('--verbose', is_flag=True, default=False, help="Augmente la verbosité")
def enable(verbose=False):
    click.secho('* Vérification de l\'état des worker', fg='blue', bold=True)
    heartbeat = queue.control.inspect().ping()
    if verbose:
        click.secho(pprint.pformat(heartbeat,  indent=4))
    if heartbeat is None:
        click.secho('  |> Les workers celery ne sont pas encore lancés', fg='yellow', bold=True)
        click.secho('* Lancement des workers', fg='blue', bold=True)
        multi = celery.bin.multi.MultiTool(quiet=True, nosplash=True)
        multi.start(['w1', '-A', 'firewall.app.queue', '-l', 'info'], cmd='celery worker')
        click.secho('* Attente du lancement des workers', fg='blue', bold=True)
        t_start = time.time()
        t_diff = 0
        while heartbeat is None:
            heartbeat = queue.control.inspect().ping()
            if heartbeat is not None:
                break
            else:
                time.sleep(0.5)
                t_diff = time.time() - t_start
                if verbose:
                    click.secho('  |> ' + str(t_diff) + 's')
        click.secho('  |> Les workers celery sont lancés', fg='green', bold=True)
    else:
        click.secho('  |> Les workers celery sont lancés', fg='green', bold=True)
        if verbose:
            click.secho(pprint.pformat(queue.control.inspect().stats(), indent=4))


@worker.command(short_help="Desactive les workers")
@click.help_option(help="Affiche ce message")
@click.option('--verbose', is_flag=True, default=False, help="Augmente la verbosité")
def disable(verbose=True):
    click.secho('* Fermeture des workers', fg='blue', bold=True)
    multi = celery.bin.multi.MultiTool(quiet=True, nosplash=True)
    multi.stop(['w1', '-A', 'firewall.app.queue', '-l', 'info'], cmd='celery worker')
    click.secho('* Attente de la fermeture des workers', fg='blue', bold=True)
    heartbeat = queue.control.inspect().ping()
    t_start = time.time()
    t_diff = 0
    while heartbeat is not None:
        heartbeat = queue.control.inspect().ping()
        if heartbeat is not None:
            break
        else:
            time.sleep(0.5)
            t_diff = time.time() - t_start
            if verbose:
                click.secho('  |> ' + str(t_diff) + 's')
    click.secho('  |> Les workers celery sont fermés', fg='green', bold=True)


@worker.command(short_help="Reload les workers", help="Affiche ce message")
@click.help_option(help="Affiche ce message")
@click.option('--verbose', is_flag=True, default=False, help="Augmente la verbosité")
def reload(verbose=False):
    click.secho('* Vérification de l\'état des worker', fg='blue', bold=True)
    heartbeat = queue.control.inspect().ping()
    if verbose:
        click.secho(pprint.pformat(heartbeat,  indent=4))
    if heartbeat is not None:
        click.secho('  |> Les workers celery sont lancés', fg='green', bold=True)
        if verbose:
            click.secho(pprint.pformat(queue.control.inspect().stats(), indent=4))
        click.secho('* Redémarage des workers', fg='blue', bold=True)
        multi = celery.bin.multi.MultiTool(quiet=True, nosplash=True)
        multi.restart(['w1', '-A', 'firewall.app.queue', '-l', 'info'], cmd='celery worker')
    else:
        click.secho('  |> Les workers celery ne sont pas encore lancés', fg='yellow', bold=True)
        click.secho('* Lancement des workers', fg='blue', bold=True)
        multi = celery.bin.multi.MultiTool(quiet=True, nosplash=True)
        multi.start(['w1', '-A', 'firewall.app.queue', '-l', 'info'], cmd='celery worker')
    click.secho('* Attente du lancement des workers', fg='blue', bold=True)
    t_start = time.time()
    t_diff = 0
    while heartbeat is None:
        heartbeat = queue.control.inspect().ping()
        if heartbeat is not None:
            break
        else:
            time.sleep(0.5)
            t_diff = time.time() - t_start
            if verbose:
                click.secho('  |> ' + str(t_diff) + 's')
    click.secho('  |> Les workers celery sont lancés', fg='green', bold=True)


@cli.command(short_help="Démarre le firewall")
@click.help_option(help="Affiche ce message")
@click.option('--verbose', is_flag=True, default=False, help="Augmente la verbosité")
def start(verbose):
    start_all()


if __name__ == '__main__':
    cli()

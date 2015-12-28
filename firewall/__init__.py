#!/usr/bin/env python3
import click

from firewall.tasks.misc.hello_world import hello
from firewall.tasks.kernel import check_and_add_module


@click.group()
@click.version_option(version='1.0.0')
def cli():
    pass


@cli.group()
def daemon():
    click.echo('Initialized the database')


@daemon.command()
def enable():
    click.echo('')


@cli.group()
def action():
    print('Initialized the database')


@action.command()
def start():
    print("Start firewall")
    hello.delay("test")
    check_and_add_module.delay("a")


if __name__ == '__main__':
    cli()

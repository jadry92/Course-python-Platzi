import click

@click.group()
def clients():
    """Manages the clients lifecycle."""
    pass


@clients.command()
@click.pass_context
def create(ctx, *arg):
    """Create a new clients."""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update a specific client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client from the list"""
    pass

all = clients

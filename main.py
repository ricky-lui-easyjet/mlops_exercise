import click
from src.train_pipeline import _train
from src.inference_pipeline import _infer
from src.tracking_server import start_tracking_server
from deployment import deploy

@click.group()
def cli():
    """Command-line interface for running pipelines."""
    pass

@click.command()
def train():
    """Run the training pipeline."""
    click.echo("Starting the training pipeline...")
    _train()
    click.echo("Training pipeline completed.")

@click.command()
def infer():
    """Run the inference pipeline."""
    click.echo("Starting the inference pipeline...")
    _infer()
    click.echo("Inference pipeline completed.")

@click.command()
def start_server():
    """Start the tracking server."""
    click.echo("Starting tracking server...")
    start_tracking_server()

@click.command()
@click.option("--host", required=True, help="Host for deployment.")
@click.option("--token", required=True, help="Token for deployment.")
def mock_deploy(host, token):
    """Mock deployment command."""
    deploy(host, token)
    click.echo("Deploying training and inference workflows...")

cli.add_command(train)
cli.add_command(infer)
cli.add_command(start_server)
cli.add_command(mock_deploy)

if __name__ == "__main__":
    cli()
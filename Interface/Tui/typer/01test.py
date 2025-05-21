import typer 
from rich import print


app = typer.Typer()


@app.callback()
def callback():
    print('Joquinha gay')

app()
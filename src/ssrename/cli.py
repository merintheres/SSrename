import typer
from pathlib import Path
from ssrename.renamer import ScreenshotRenamer

app = typer.Typer()

@app.command()
def rename(
    path: Path,
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without renaming"),
):
    renamer = ScreenshotRenamer(path=path, dry_run=dry_run)
    renamer.run()

def main():
    app()

if __name__ == "__main__":
    main()

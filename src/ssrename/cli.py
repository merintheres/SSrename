import typer
from pathlib import Path
from ssrename.renamer import ScreenshotRenamer

app = typer.Typer()

@app.command()
def rename(
    path: Path,
    dry_run: bool = typer.Option(False, "--dry-run"),
    limit: int | None = typer.Option(None, "--limit"),
    verbose: bool = typer.Option(False, "--verbose"),
    ocr_only: bool = typer.Option(False, "--ocr-only"),
    ai_only: bool = typer.Option(False, "--ai-only"),
    max_words: int = typer.Option(5, "--max-words")
):
    if ocr_only and ai_only:
        raise typer.BadParameter("Use only one of --ocr-only or --ai-only")

    ScreenshotRenamer(
        path=path,
        dry_run=dry_run,
        limit=limit,
        verbose=verbose,
        ocr_only=ocr_only,
        ai_only=ai_only,
        max_words=max_words
    ).run()

def main():
    app()

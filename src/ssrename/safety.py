class SafetyManager:
    def __init__(self, console):
        self.console = console

    def preview(self, images, dry_run):
        if not images:
            self.console.print("[yellow]No images found[/yellow]")
            return

        for idx, img in enumerate(images, start=1):
            new_name = f"image_{idx}{img.suffix}"
            if dry_run:
                self.console.print(f"[blue]DRY RUN[/blue] {img.name} → {new_name}")
            else:
                img.rename(img.with_name(new_name))
                self.console.print(f"[green]RENAMED[/green] {img.name} → {new_name}")

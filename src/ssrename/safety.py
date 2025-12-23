class SafetyManager:
    def __init__(self, console):
        self.console = console

    def preview(self, images, name_generator, dry_run, verbose=False):
        used = {}
        results = name_generator(images)

        for r in results:
            img = r["image"]
            name = self._resolve(r["filename"], used)

            if verbose:
                self.console.print(
                    f"[cyan]{img.name}[/cyan] "
                    f"(source={r['source']}, words={r['words']}, type={r['type']})"
                )

            if dry_run:
                self.console.print(f"[blue]DRY RUN[/blue] {img.name} → {name}")
            else:
                img.rename(img.with_name(name))
                self.console.print(f"[green]RENAMED[/green] {img.name} → {name}")

    def _resolve(self, name, used):
        if name not in used:
            used[name] = 0
            return name
        used[name] += 1
        stem, ext = name.rsplit(".", 1)
        return f"{stem}_{used[name]}.{ext}"

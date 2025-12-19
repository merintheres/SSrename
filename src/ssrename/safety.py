class SafetyManager:
    def __init__(self, console):
        self.console = console

    def preview(self, images, name_generator, dry_run):
        used = {}

        new_names = name_generator(images)

        for img, name in zip(images, new_names):
            final_name = self._resolve_duplicate(name, used)

            if dry_run:
                self.console.print(f"[blue]DRY RUN[/blue] {img.name} → {final_name}")
            else:
                img.rename(img.with_name(final_name))
                self.console.print(f"[green]RENAMED[/green] {img.name} → {final_name}")

    def _resolve_duplicate(self, name, used):
        if name not in used:
            used[name] = 1
            return name

        count = used[name]
        used[name] += 1

        stem, suffix = name.rsplit(".", 1)
        return f"{stem}_{count}.{suffix}"

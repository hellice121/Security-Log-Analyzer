from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def display_banner():
    title = Text("SENTINELLOG", justify="center", style="bold cyan")
    subtitle = Text(
        "Security Log Analysis & Detection Tool",
        justify="center",
        style="white"
    )
    version = Text("Version 0.1.0", justify="center", style="dim")

    banner = Text()
    banner.append_text(title)
    banner.append("\n")
    banner.append_text(subtitle)
    banner.append("\n\n")
    banner.append_text(version)

    panel = Panel(
        banner,
        border_style="cyan",
        padding=(1, 4),
        title="[bold]Security Analyzer[/bold]",
        subtitle="Analyze • Detect • Assess"
    )

    console.print(panel)

def get_log_path():
    console.print(
        Panel(
            "[bold]Enter the path to the access log you want to analyze.[/bold]\n"
            "[dim]Example: C:\\logs\\access.log[/dim]",
            title="[cyan]Log File Selection[/cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )

    path = Prompt.ask("[bold cyan]Log file path[/bold cyan]")

    # Useful when users copy a Windows path with surrounding quotes
    path = path.strip().strip('"').strip("'")
    
    return path


def display_security_alert(ip, obj):
    detections = []

    if obj.brute_force:
        detections.append("Brute Force")

    if obj.reconnaissance:
        detections.append("Reconnaissance")

    summary = (
        f"[bold]IP Address:[/bold]  {ip}\n"
        f"[bold]Status:[/bold]      [red bold]FLAGGED[/red bold]\n"
        f"[bold]Detections:[/bold]  {','.join(obj.detection)}"
    )

    console.print(
        Panel(
            summary,
            title="[red bold]SECURITY ALERT[/red bold]",
            border_style="red"
        )
    )

    if obj.brute_force:
        console.print("\n[bold red]BRUTE FORCE[/bold red]")
        console.print(f"Total Attempts:  {obj.t_attempts}")
        console.print(f"Failed Attempts: {obj.failed_attempts}")

    if obj.reconnaissance:
        console.print("\n[bold yellow]RECONNAISSANCE[/bold yellow]")

        table = Table()
        table.add_column("Resource")
        table.add_column("Requests", justify="right")

        for resource, count in obj.suspicious_resources.items():
            table.add_row(resource, str(count))

        console.print(table)

    if obj.method_abuse:
        console.print("\n[bold yellow]HTTP METHOD ABUSE[/bold yellow]")

        table = Table()
        table.add_column("Suspicious Method")
        table.add_column("Requests", justify="right")

        for method, count in obj.suspicious_methods.items():
            table.add_row(method, str(count))

        console.print(table)

def display_log_summary(valid, non_valid):
    total = valid + non_valid

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2)
    )

    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    table.add_row("Total Log Entries", str(total))
    table.add_row("[green]Valid Logs[/green]", f"[green]{valid}[/green]")
    table.add_row("[red]Invalid Logs[/red]", f"[red]{non_valid}[/red]")

    if total > 0:
        valid_percentage = (valid / total) * 100
        table.add_row(
            "Successfully Parsed",
            f"{valid_percentage:.1f}%"
        )

    panel = Panel(
        table,
        title="[bold cyan]Log Processing Summary[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    )

    console.print()
    console.print(panel)
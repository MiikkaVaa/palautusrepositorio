from rich.console import Console
from rich.table import Table
from rich import box

from player_reader import PlayerReader
from player_stats import PlayerStats


def _season_choices(start: int = 2018, end: int = 2026) -> str:
    return "/".join(f"{y}-{(y + 1) % 100:02d}" for y in range(start, end))


def _ask_season(console: Console, default: str = "2024-25") -> str:
    choices = _season_choices()
    prompt = f"Season [[][magenta]{choices}[/][]] ([green]{default}[/]): "
    return console.input(prompt).strip() or default


def _ask_nationality(console: Console, reader: PlayerReader) -> str:
    codes = sorted({p.nationality for p in reader.get_players()})
    prompt = f"Nationality [[][magenta]{'/'.join(codes)}[/][]]: "
    return console.input(prompt).strip().upper()


def _build_table(title: str) -> Table:
    table = Table(title=title, box=box.SQUARE, header_style="bold")
    table.add_column("name", style="cyan")
    table.add_column("team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")
    return table


def _render(console: Console, table: Table, players):
    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))
    console.print()
    console.print(table)
    console.print()


def main() -> None:
    console = Console()
    season = _ask_season(console)

    reader = PlayerReader(
        f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    )
    stats = PlayerStats(reader)

    nationality = _ask_nationality(console, reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = _build_table(f"Season {season} players from {nationality}")
    _render(console, table, players)


if __name__ == "__main__":
    main()

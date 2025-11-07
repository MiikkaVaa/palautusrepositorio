from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich import box

def _season_choices(start=2018, end=2026):
    return "/".join(f"{y}-{(y+1)%100:02d}" for y in range(start,end))

def main():
    console = Console()
    season_default = "2024-25"
    season_choices = _season_choices()

    season = console.input(
        f"Season [[magenta]{season_choices}[/]] ([green]{season_default}[/]): "
    ).strip() or season_default


    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nat_codes = sorted({p.nationality for p in reader.get_players()})
    nat_list = "/".join(nat_codes)
    nationality = console.input(
        f"Nationality [[magenta]{nat_list}[/]]: "
    ).strip().upper()
    
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(
        title=f"Season {season} players from {nationality}",
        box=box.SQUARE,
        header_style="bold",
    )
    table.add_column("Released", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))
    
    console.print()
    console.print(table)
    console.print()


if __name__ == "__main__":
    main()

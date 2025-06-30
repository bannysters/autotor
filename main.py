import os
import sys
import re
import time
import webbrowser
import requests
import pyfiglet
from rich import print
from rich.table import Table
from rich.console import Console

api_key = "" # Get a key at https://www.omdbapi.com/apikey.aspx

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    Console().print("<AUTOTOR> Made by bannisters", style="bold white", justify="left")
    Console().print("<AUTOTOR> This program uses public apis to find the best quality torrent of a movie with only its name, then automatically download it.", style="bold white", justify="left")
    print("----------------------------")

def fetch_movie_info(title):
    url = f"https://www.omdbapi.com/?t={requests.utils.quote(title)}&apikey={api_key}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def print_movie_info(info):
    c = Console()
    c.print(f"[bold green]Title:[/bold green] {info.get('Title','N/A')}")
    c.print(f"[bold green]Year:[/bold green]  {info.get('Year','N/A')}")
    c.print(f"[bold green]Genre:[/bold green] {info.get('Genre','N/A')}")
    c.print(f"[bold green]Plot:[/bold green]  {info.get('Plot','N/A')}\n")
    c.print(f"[bold blue]Awards:[/bold blue]     {info.get('Awards','N/A')}")
    c.print(f"[bold blue]Box Office:[/bold blue] {info.get('BoxOffice','N/A')}")
    tbl = Table(show_header=False)
    tbl.add_column("Source", style="cyan")
    tbl.add_column("Rating", style="yellow")
    for r in info.get("Ratings", []):
        tbl.add_row(r["Source"], r["Value"])
    c.print(tbl)
    c.print("\n[bold red]Searching for torrent…\n")

def search_yts(title, year=None):
    api = "https://yts.mx/api/v2/list_movies.json"
    resp = requests.get(api, params={"query_term": title, "limit":50})
    resp.raise_for_status()
    movies = resp.json().get("data",{}).get("movies",[])
    candidates = []
    for m in movies:
        if year and str(m.get("year")) != str(year):
            continue
        for t in m.get("torrents", []):
            if t.get("quality") == "1080p":
                magnet = (
                    f"magnet:?xt=urn:btih:{t['hash']}"
                    f"&dn={requests.utils.quote(m['title_long'])}"
                    "&tr=udp://tracker.openbittorrent.com:80"
                )
                candidates.append({
                    "title": m["title_long"],
                    "seeds": t["seeds"],
                    "magnet": magnet
                })
    return sorted(candidates, key=lambda x: x["seeds"], reverse=True)


def main():
    clear_screen()
    print_banner()

    query = input("Enter movie name >> ").strip()
    if not query:
        print("[red]No movie name provided.. closing[/red]")
        sys.exit(1)

    info = fetch_movie_info(query)
    clear_screen(); print_banner()
    print_movie_info(info)
    year = info.get("Year","")[:4]

    candidates = search_yts(query, year)
    if not candidates:
        print("[yellow]No good torrents found on YTS.[/yellow]")
        sys.exit(0)

    best = candidates[0]
    print(f"[bold]Best match:[/bold] {best['title']} — Seeds: {best['seeds']}")
    choice = input("Open this magnet in your torrent client? (y/N) ").strip().lower()
    if choice == 'y':
        print(f"[green]Launching magnet link…[/green]\n")
        webbrowser.open(best["magnet"])
        print("[bold blue]If nothing happens, make sure you have a torrent client installed like qbittorrent[/bold blue]")
        time.sleep(2)
    else:
        print("[cyan]Closing..[/cyan]")

if __name__ == "__main__":
    main()

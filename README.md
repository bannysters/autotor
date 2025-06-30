# AUTOTOR

A **Python CLI tool** that uses public APIs to find the **best quality torrent** of a movie by **name only** and **automatically downloads it**.

---

## Features

✅ Fetches **movie details** (plot, year, ratings, awards) from **OMDb API**
✅ Finds **best 1080p torrents with the highest seeds** using **YTS**
✅ Automatically **launches magnet link** in your torrent client (`qBittorrent`, `Transmission`, etc.)
✅ Works on **Windows, Linux, macOS**
✅ Uses **clean Rich/pyfiglet output** for aesthetic CLI display

---

## Requirements

* Python 3.8+
* Install dependencies:

```bash
pip install requests rich pyfiglet
```

---

## Setup

1️⃣ Get a **free OMDb API key**:
Register at [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx).

2️⃣ Paste your key in the script:

```python
api_key = "YOUR_OMDB_API_KEY"
```

---

## Usage

Run:

```bash
python autotor.py
```

* Enter the **movie name** when prompted.
* Review fetched movie details (plot, year, ratings, awards).
* The script will automatically search for **1080p torrents** with the **highest seeds** on YTS.
* You will be prompted to **open the magnet link** in your default torrent client.

---

## Example

```
Enter movie name >> blade runner 2049

Best match: Blade Runner 2049 (2017) — Seeds: 3500

Open this magnet in your torrent client? (y/N)
```

If you type `y`, your torrent client will open and begin downloading automatically.

---

## Notes

* This tool **does not host or distribute copyrighted material**.
* It **only uses public APIs and magnet links**.
* **Use responsibly and respect your local laws.**

---

## License

MIT License

---

## Credits

**AUTOTOR**
Made by bannisters.
Uses:

* [OMDb API](https://www.omdbapi.com/)
* [YTS API](https://yts.mx/api)
* [Rich](https://github.com/Textualize/rich) for CLI formatting
* [pyfiglet](https://github.com/pwaller/pyfiglet) for banners

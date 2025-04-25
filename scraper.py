# Updated scraper to follow best practice (user-agent, delay, safe scraping)

import requests
from bs4 import BeautifulSoup
import time
import random

def fetch_odds_from_bookmaker(url, bookmaker_name):
    """
    Fetch odds from a single bookmaker website.
    """

    # Polite bot header
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ArbitrageBot/1.0; +https://your-arbitrage-site.com)"
    }

    try:
        # Delay to avoid overwhelming the server
        time.sleep(random.uniform(1.5, 3.5))

        # Make the request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Placeholder logic - should be replaced with bookmaker-specific parsing
        odds = []

        for event in soup.select(".event-row"):
            team1 = event.select_one(".team1").text.strip()
            team2 = event.select_one(".team2").text.strip()
            odds1 = float(event.select_one(".odds1").text.strip())
            odds2 = float(event.select_one(".odds2").text.strip())

            odds.append({
                "bookmaker": bookmaker_name,
                "event": f"{team1} vs {team2}",
                "odds": [odds1, odds2]
            })

        return odds

    except Exception as e:
        print(f"Error fetching odds from {bookmaker_name}: {e}")
        return []

def get_all_odds():
    """
    Combine odds from multiple bookmakers.
    """
    all_odds = []

    # Replace these with real bookmaker URLs and make sure they're okay to scrape
    bookmakers = [
        {"name": "Bookmaker A", "url": "https://example-bookmaker-a.com/odds"},
        {"name": "Bookmaker B", "url": "https://example-bookmaker-b.com/odds"}
    ]

    for bm in bookmakers:
        odds = fetch_odds_from_bookmaker(bm["url"], bm["name"])
        all_odds.extend(odds)

    return all_odds

def find_arbitrage_opportunities(odds_list):
    """
    Finds arbitrage opportunities across bookmakers.
    """
    arbitrage_opps = []

    # This example assumes the same event appears multiple times (from different bookmakers)
    event_map = {}

    for entry in odds_list:
        event = entry["event"]
        if event not in event_map:
            event_map[event] = []
        event_map[event].append(entry)

    for event, entries in event_map.items():
        if len(entries) < 2:
            continue

        best_odds = [0, 0]
        best_bookmakers = ["", ""]

        for entry in entries:
            if entry["odds"][0] > best_odds[0]:
                best_odds[0] = entry["odds"][0]
                best_bookmakers[0] = entry["bookmaker"]
            if entry["odds"][1] > best_odds[1]:
                best_odds[1] = entry["odds"][1]
                best_bookmakers[1] = entry["bookmaker"]

        inv_sum = (1 / best_odds[0]) + (1 / best_odds[1])
        if inv_sum < 1:
            arbitrage_opps.append({
                "event": event,
                "odds": best_odds,
                "bookmakers": best_bookmakers,
                "profit_margin": round((1 - inv_sum) * 100, 2)
            })

    return arbitrage_opps

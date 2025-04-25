# scraper.py
def scrape_tab_nz():
    return [
        {"event": "Team A vs Team B", "outcome": "Team A", "odds": 2.1, "bookmaker": "TAB NZ"},
        {"event": "Team A vs Team B", "outcome": "Team B", "odds": 1.8, "bookmaker": "TAB NZ"}
    ]

def scrape_bet365():
    return [
        {"event": "Team A vs Team B", "outcome": "Team A", "odds": 1.95, "bookmaker": "Bet365"},
        {"event": "Team A vs Team B", "outcome": "Team B", "odds": 2.0, "bookmaker": "Bet365"}
    ]

def scrape_unibet():
    return [
        {"event": "Team A vs Team B", "outcome": "Team A", "odds": 2.05, "bookmaker": "Unibet"},
        {"event": "Team A vs Team B", "outcome": "Team B", "odds": 1.9, "bookmaker": "Unibet"}
    ]
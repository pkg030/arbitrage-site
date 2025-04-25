# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape_tab_nz, scrape_bet365, scrape_unibet
from arbitrage import find_arbitrage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/arbitrage")
def get_arbitrage():
    tab = scrape_tab_nz()
    bet365 = scrape_bet365()
    unibet = scrape_unibet()

    all_odds = tab + bet365 + unibet
    arbs = find_arbitrage(all_odds)
    return {"arbitrage": arbs}


# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape_tab_nz, scrape_bet365, scrape_unibet
from arbitrage import find_arbitrage
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add logging for debugging
logging.basicConfig(level=logging.INFO)

@app.get("/arbitrage")
def get_arbitrage():
    try:
        logging.info("Starting arbitrage scraping...")
        
        tab = scrape_tab_nz()
        bet365 = scrape_bet365()
        unibet = scrape_unibet()

        if not tab or not bet365 or not unibet:
            logging.warning("Some of the scraping functions returned empty data.")

        all_odds = tab + bet365 + unibet
        logging.info(f"Total odds collected: {len(all_odds)}")

        arbs = find_arbitrage(all_odds)
        
        if not arbs:
            logging.warning("No arbitrage opportunities found.")
        
        return {"arbitrage": arbs}

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return {"error": "An error occurred while processing the request."}

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Welcome to the Arbitrage Finder API</h1><p>Use <code>/arbitrage</code> to find opportunities.</p>"

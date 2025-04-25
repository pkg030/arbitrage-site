# arbitrage.py
def find_arbitrage(odds_list):
    events = {}
    for bet in odds_list:
        event = bet["event"]
        outcome = bet["outcome"]

        if event not in events:
            events[event] = {}

        if outcome not in events[event] or bet["odds"] > events[event][outcome]["odds"]:
            events[event][outcome] = bet

    arbitrage_opportunities = []
    for event, outcomes in events.items():
        if len(outcomes) < 2:
            continue

        inv_sum = sum(1 / outcomes[o]["odds"] for o in outcomes)
        if inv_sum < 1:
            arbitrage_opportunities.append({
                "event": event,
                "bets": list(outcomes.values()),
                "profit_percent": round((1 - inv_sum) * 100, 2)
            })

    return arbitrage_opportunities
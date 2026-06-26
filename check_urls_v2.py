#!/usr/bin/env python3
"""Save this script locally and run it with python3."""
import urllib.request, urllib.error, json, ssl

ctx = ssl._create_unverified_context()  # allow self-signed certs

urls = [
    ("1. Bloomberg Billionaires - Musk", "https://www.bloomberg.com/billionaires/profiles/elon-musk/"),
    ("2. Forbes Billionaires - Musk", "https://www.forbes.com/profile/elon-musk/"),
    ("3. SpaceX Falcon 1 Flight 4 - Sept 2008 success", "https://www.spacex.com/news/2008/09/28/flight-4-launch-update/"),
    ("3b. SpaceX Falcon 1 Flight 4 (alternate)", "https://www.spacex.com/launches/f1-flight4/"),
    ("3c. SpaceX history - Falcon 1", "https://www.spacex.com/vehicles/falcon-1/"),
    ("4. NASA Awards $1.6B SpaceX CRS contract", "https://www.nasa.gov/news-release/nasa-awards-spacex-commercial-resupply-contract/"),
    ("4b. NASA CRS overview", "https://www.nasa.gov/mission/commercial-resupply-services/"),
    ("5. Tesla Model 3 production hell - Bloomberg", "https://www.bloomberg.com/graphics/2018-tesla-model-3/"),
    ("5b. Tesla Q2 2018 earnings (production hell mention)", "https://ir.tesla.com/press-release/tesla-q2-2018-vehicle-production-and-deliveries"),
    ("6a. ARK Invest Big Ideas 2023", "https://ark-invest.com/big-ideas-2023/"),
    ("6b. ARK Invest: Elon Musk trillionaire", "https://www.ark-invest.com/articles/analyst-research/the-trillion-dollar-opportunity"),
    ("6c. Informa Connect trillion dollar club", "https://www.informa.com.au/insight/the-trillion-dollar-club/"),
    ("7a. Ashlee Vance biography 'Elon Musk'", "https://www.harpercollins.com/products/elon-musk-ashlee-vance"),
    ("7b. 'Elon Musk' on Amazon", "https://www.amazon.com/Elon-Musk-SpaceX-Fantastic-Future/dp/0062301233"),
    ("8. Wired article on Musk academic references", "https://www.wired.com/story/elon-musk-research-books-papers/"),
]

results = {}
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        resp = urllib.request.urlopen(req, timeout=15, context=ctx)
        results[name] = {"status": resp.status, "final_url": resp.url, "ok": True}
    except urllib.error.HTTPError as e:
        results[name] = {"status": e.code, "final_url": url, "ok": True, "note": f"HTTP {e.code}"}
    except Exception as e:
        results[name] = {"status": "FAIL", "final_url": url, "ok": False, "note": str(e)[:120]}

print(json.dumps(results, indent=2))
print("\n--- SUMMARY ---")
ok = sum(1 for v in results.values() if v.get("ok"))
print(f"Responded: {ok}/{len(urls)}")

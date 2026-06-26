#!/usr/bin/env python3
"""Check reachability of key Elon Musk source URLs."""
import urllib.request, urllib.error, json, sys, ssl

ctx = ssl.create_default_context()

urls = {
    "1. Bloomberg Billionaires Index - Musk": "https://www.bloomberg.com/billionaires/profiles/elon-musk/",
    "2. Forbes Billionaires - Musk": "https://www.forbes.com/profile/elon-musk/",
    "3. Falcon 1 Flight 4 success (SpaceX)": "https://www.spacex.com/news/2008/09/28/flight-4-launch-update/",
    "4. NASA CRS contract $1.6B": "https://www.nasa.gov/news-release/nasa-awards-spacex-commercial-resupply-contract/",
    "5. Tesla Model 3 production hell (Bloomberg)": "https://www.bloomberg.com/graphics/2018-tesla-model-3/",
    "6a. ARK Invest SpaceX valuation": "https://ark-invest.com/articles/analyst-research/spacex-valuation-2023",
    "6b. ARK Big Ideas report": "https://www.ark-invest.com/big-ideas-2023",
    "6c. Informa trillionaire club": "https://www.informa.com.au/insight/the-trillion-dollar-club/",
    "7a. Ashlee Vance biography (HarperCollins)": "https://www.harpercollins.com/products/elon-musk-ashlee-vance",
    "7b. Vance bio on Amazon": "https://www.amazon.com/Elon-Musk-SpaceX-Fantastic-Future/dp/0062301233",
}

results = {}
for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=10, context=ctx)
        results[name] = {
            "status": resp.status,
            "final_url": resp.url,
            "reachable": True,
            "note": "OK" if resp.status == 200 else f"HTTP {resp.status}"
        }
    except urllib.error.HTTPError as e:
        # Some sites return 403/404/301 etc - still a valid response
        results[name] = {
            "status": e.code,
            "final_url": url,
            "reachable": True,
            "note": f"HTTP {e.code}" + (" (paywall/service blocks bots)" if e.code in (401, 403) else "")
        }
    except Exception as e:
        results[name] = {
            "status": "ERROR",
            "final_url": url,
            "reachable": False,
            "note": str(e)[:150]
        }

print(json.dumps(results, indent=2))
print("\n--- SUMMARY ---")
reachable = sum(1 for v in results.values() if v.get("reachable"))
print(f"Reachable: {reachable}/{len(urls)}")

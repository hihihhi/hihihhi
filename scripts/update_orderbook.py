"""Refresh the order book drawn on the water in assets/header.svg from Binance's public depth API.

Only the 28 order-book <rect> elements (14 bid bands, 14 ask bands) are rewritten. Everything
else in the SVG stays byte-identical. Run by .github/workflows/orderbook.yml, which commits as
github-actions[bot].

    python3 scripts/update_orderbook.py assets/header.svg

data-api.binance.vision is used because api.binance.com answers 451 to US-hosted runners.
"""
import json
import random
import re
import sys
import urllib.request

URL = 'https://data-api.binance.vision/api/v3/depth?symbol=BTCUSDT&limit=5000'
BPS = [1, 2, 4, 7, 10, 15, 20, 28, 36, 45, 55, 66, 80, 95]   # same bands as the site's bundled snapshot
BAR = 190                                                    # longest bar, px, as drawn by the site
RECT = re.compile(r'<rect x="([^"]*)" y="([^"]*)" width="([^"]*)" height="2" fill="url\(#(bid|ask)\)">.*?</rect>', re.S)


def parse_book(raw):
    """Binance depth JSON -> {'bids': [(price, qty)...] desc, 'asks': [...] asc}; ValueError if unusable."""
    try:
        bids = sorted(((float(p), float(q)) for p, q in raw['bids'] if float(q) > 0), reverse=True)
        asks = sorted((float(p), float(q)) for p, q in raw['asks'] if float(q) > 0)
    except (KeyError, TypeError, ValueError) as e:
        raise ValueError(f'malformed depth: {e}') from e
    if not bids or not asks:
        raise ValueError('empty side')
    if bids[0][0] >= asks[0][0]:
        raise ValueError('crossed book')
    return {'bids': bids, 'asks': asks}


def bands(book, bps):
    """Mid and cumulative size within each distance (basis points) of mid, per side."""
    mid = (book['bids'][0][0] + book['asks'][0][0]) / 2
    bid = [sum(q for p, q in book['bids'] if p >= mid * (1 - b / 1e4)) for b in bps]
    ask = [sum(q for p, q in book['asks'] if p <= mid * (1 + b / 1e4)) for b in bps]
    return mid, bid, ask


def rewrite(svg, book):
    """Replace the order-book block; ValueError if the SVG does not hold exactly one such block."""
    rects = list(RECT.finditer(svg))
    if len(rects) != 2 * len(BPS):
        raise ValueError(f'expected {2 * len(BPS)} order-book rects, found {len(rects)}')
    start, end = rects[0].start(), rects[-1].end()
    asks = [m for m in rects if m.group(4) == 'ask']
    xt = float(asks[0].group(1)) - 3                          # asks start 3 px right of t = now
    ys = [m.group(2) for m in rects if m.group(4) == 'bid']
    _, bid, ask = bands(book, BPS)
    dmax = max(bid + ask) or 1
    rng = random.Random(42)                                   # same shimmer every run: diffs show only the book
    f = lambda v: f'{v:.1f}'
    out = []
    for yy, bq, aq in zip(ys, bid, ask):
        for side, q in (('bid', bq), ('ask', aq)):
            ln = max(q / dmax * BAR, 3.5)
            vals = [ln * v for v in (1, 0.9 + 0.08 * rng.random(), 1.04 + 0.04 * rng.random(), 0.95, 1)]
            dur = 2.2 + rng.random() * 1.8
            if side == 'bid':
                xs = ';'.join(f(xt - v) for v in vals)
                ws = ';'.join(f(v - 3) for v in vals)
                out.append(f'<rect x="{f(xt - ln)}" y="{yy}" width="{f(ln - 3)}" height="2" fill="url(#bid)">'
                           f'<animate attributeName="x" values="{xs}" dur="{dur:.2f}s" repeatCount="indefinite"/>'
                           f'<animate attributeName="width" values="{ws}" dur="{dur:.2f}s" repeatCount="indefinite"/></rect>')
            else:
                ws = ';'.join(f(v) for v in vals)
                out.append(f'<rect x="{f(xt + 3)}" y="{yy}" width="{f(ln)}" height="2" fill="url(#ask)">'
                           f'<animate attributeName="width" values="{ws}" dur="{dur:.2f}s" repeatCount="indefinite"/></rect>')
    return svg[:start] + '\n'.join(out) + svg[end:]


def main(path):
    req = urllib.request.Request(URL, headers={'User-Agent': 'oscar-chw-header'})
    with urllib.request.urlopen(req, timeout=20) as r:
        book = parse_book(json.load(r))
    svg = open(path, encoding='utf-8').read()
    new = rewrite(svg, book)
    if new != svg:
        open(path, 'w', encoding='utf-8').write(new)
    mid = (book['bids'][0][0] + book['asks'][0][0]) / 2
    print(f'order book refreshed: mid {mid:,.2f}, {"changed" if new != svg else "unchanged"}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'assets/header.svg')

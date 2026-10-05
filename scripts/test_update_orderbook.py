"""Tests for update_orderbook.py. Run: python3 -m unittest discover -s scripts -p 'test_*.py'"""
import os
import re
import unittest

from update_orderbook import BPS, bands, parse_book, rewrite

HERE = os.path.dirname(os.path.abspath(__file__))
SVG = open(os.path.join(HERE, '..', 'assets', 'header.svg'), encoding='utf-8').read()
RECT = re.compile(r'<rect x="[^"]*" y="[^"]*" width="[^"]*" height="2" fill="url\(#(?:bid|ask)\)">.*?</rect>', re.S)


def book(mid=60000.0, levels=400, tick=1.0, qty=0.5):
    return {'bids': [[f'{mid - 0.5 - i * tick:.2f}', f'{qty}'] for i in range(levels)],
            'asks': [[f'{mid + 0.5 + i * tick:.2f}', f'{qty}'] for i in range(levels)]}


class Bands(unittest.TestCase):
    def test_cumulative_size_within_each_distance(self):
        b = parse_book({'bids': [['99.99', '1'], ['99.9', '2'], ['99', '5']], 'asks': [['100.01', '1'], ['100.1', '3'], ['101', '7']]})
        mid, bid, ask = bands(b, [2, 20, 200])
        self.assertAlmostEqual(mid, 100.0)
        self.assertEqual(bid, [1, 3, 8])
        self.assertEqual(ask, [1, 4, 11])

    def test_monotone(self):
        _, bid, ask = bands(parse_book(book()), BPS)
        self.assertEqual(bid, sorted(bid))
        self.assertEqual(ask, sorted(ask))


class ParseBook(unittest.TestCase):
    def test_refuses_empty_crossed_or_malformed(self):
        for raw in ({}, {'bids': [], 'asks': [['1', '1']]}, {'bids': [['2', '1']], 'asks': [['1', '1']]},
                    {'bids': [['x', '1']], 'asks': [['2', '1']]}):
            with self.assertRaises(ValueError):
                parse_book(raw)


class Rewrite(unittest.TestCase):
    def test_changes_only_the_order_book_block(self):
        out = rewrite(SVG, parse_book(book()))
        old, new = list(RECT.finditer(SVG)), list(RECT.finditer(out))
        self.assertEqual(len(old), 2 * len(BPS))
        self.assertEqual(len(new), len(old))
        self.assertEqual(SVG[:old[0].start()], out[:new[0].start()])          # everything before: byte-identical
        self.assertEqual(SVG[old[-1].end():], out[new[-1].end():])            # everything after: byte-identical
        self.assertNotEqual(SVG, out)                                          # and the bars did change

    def test_rows_keep_their_positions(self):
        out = rewrite(SVG, parse_book(book()))
        ys = lambda s: re.findall(r'<rect x="[^"]*" y="([^"]*)" width="[^"]*" height="2" fill="url\(#(?:bid|ask)\)">', s)
        self.assertEqual(ys(SVG), ys(out))

    def test_lengths_follow_the_book(self):
        thin, thick = parse_book(book(qty=0.1)), parse_book(book(qty=0.1))
        thick['bids'] = [(p, q * (5 if i > 200 else 1)) for i, (p, q) in enumerate(thick['bids'])]   # deep bids far from mid
        w = lambda s: [float(x) for x in re.findall(r'width="([0-9.]+)" height="2" fill="url\(#bid\)"', s)]
        self.assertLess(w(rewrite(SVG, thick))[5], w(rewrite(SVG, thin))[5])  # a near band shrinks relative to the deep max

    def test_deterministic(self):
        b = parse_book(book())
        self.assertEqual(rewrite(SVG, b), rewrite(SVG, b))

    def test_refuses_an_svg_without_the_block(self):
        with self.assertRaises(ValueError):
            rewrite('<svg></svg>', parse_book(book()))


if __name__ == '__main__':
    unittest.main()

import unittest

from skills.search_term_mining import mine_search_terms


class SearchTermMiningTest(unittest.TestCase):
    def test_classifies_negative_expansion_and_watch_terms(self):
        rows = [
            {
                "search_term": "cheap cable",
                "spend": "35",
                "sales": "0",
                "orders": "0",
                "clicks": "42",
            },
            {
                "search_term": "fast charging travel adapter",
                "spend": "20",
                "sales": "180",
                "orders": "6",
                "clicks": "50",
            },
            {
                "search_term": "usb c adapter",
                "spend": "12",
                "sales": "35",
                "orders": "1",
                "clicks": "44",
            },
        ]

        result = mine_search_terms(rows)

        self.assertEqual(result["negative_candidates"][0]["term"], "cheap cable")
        self.assertEqual(
            result["expansion_candidates"][0]["term"],
            "fast charging travel adapter",
        )
        self.assertEqual(result["watch_terms"][0]["term"], "usb c adapter")


if __name__ == "__main__":
    unittest.main()

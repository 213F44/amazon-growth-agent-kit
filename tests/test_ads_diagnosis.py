import unittest

from skills.ads_diagnosis import diagnose_ads


class AdsDiagnosisTest(unittest.TestCase):
    def test_flags_high_acos_and_wasted_spend(self):
        rows = [
            {
                "campaign": "Auto Research",
                "spend": "80",
                "sales": "100",
                "clicks": "90",
                "impressions": "12000",
                "orders": "1",
                "cpc": "0.89",
            },
            {
                "campaign": "Exact Hero",
                "spend": "40",
                "sales": "400",
                "clicks": "120",
                "impressions": "6000",
                "orders": "16",
                "cpc": "0.33",
            },
        ]

        result = diagnose_ads(rows)

        self.assertEqual(result["summary"]["campaigns"], 2)
        self.assertIn("High ACOS", result["campaigns"][0]["flags"])
        self.assertIn("Wasted spend risk", result["campaigns"][0]["flags"])
        self.assertIn("Scale candidate", result["campaigns"][1]["flags"])


if __name__ == "__main__":
    unittest.main()

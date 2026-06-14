import unittest

from skills.creative_brief import build_creative_brief
from skills.listing_optimization import optimize_listing
from skills.review_insight import analyze_reviews


class ContentSkillsTest(unittest.TestCase):
    def test_listing_review_and_creative_outputs_are_actionable(self):
        listing = {
            "title": "65W Travel Charger",
            "bullets": [
                "Compact charger for work trips",
                "Includes foldable plug and dual ports",
            ],
            "keywords": ["usb c charger", "fast charging", "travel adapter"],
            "rating": 4.1,
        }
        search_terms = [
            {"term": "fast charging travel adapter"},
            {"term": "usb c charger"},
        ]
        reviews = [
            {"rating": "5", "text": "Fast charging and compact for travel."},
            {"rating": "2", "text": "Gets hot and instructions are confusing."},
        ]

        review_result = analyze_reviews(reviews)
        listing_result = optimize_listing(listing, search_terms, review_result)
        creative_result = build_creative_brief(listing_result, review_result)

        self.assertIn("Rating below trust threshold", listing_result["risks"])
        self.assertIn("heat", review_result["pain_points"])
        self.assertIn("Fast charging", creative_result["main_image_brief"])
        self.assertIn("travel", creative_result["lifestyle_image_brief"].lower())
        self.assertEqual(len(creative_result["short_video_script"]), 3)


if __name__ == "__main__":
    unittest.main()

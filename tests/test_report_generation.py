import tempfile
import unittest
from pathlib import Path

import agent


class ReportGenerationTest(unittest.TestCase):
    def test_agent_generates_report_with_all_sections(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "growth_report.md"
            report = agent.run(output_path=output_path)

            self.assertTrue(output_path.exists())
            self.assertIn("Ads Diagnosis", report)
            self.assertIn("Search Term Mining", report)
            self.assertIn("Listing Optimization", report)
            self.assertIn("Review Insights", report)
            self.assertIn("Creative Brief", report)
            self.assertIn("Weekly Action Plan", report)


if __name__ == "__main__":
    unittest.main()

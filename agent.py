import csv
import json
from pathlib import Path

from skills.ads_diagnosis import diagnose_ads
from skills.creative_brief import build_creative_brief
from skills.listing_optimization import optimize_listing
from skills.review_insight import analyze_reviews
from skills.search_term_mining import mine_search_terms
from skills.weekly_growth_report import build_weekly_report


ROOT = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = ROOT / "data"
DEFAULT_OUTPUT_PATH = ROOT / "outputs" / "growth_report.md"


def load_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing CSV file: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def load_json(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def run(output_path=None, data_dir=None):
    data_dir = Path(data_dir) if data_dir else DEFAULT_DATA_DIR
    output_path = Path(output_path) if output_path else DEFAULT_OUTPUT_PATH

    ads_rows = load_csv(data_dir / "ads_report.csv")
    search_rows = load_csv(data_dir / "search_terms.csv")
    listing = load_json(data_dir / "listing.json")
    review_rows = load_csv(data_dir / "reviews.csv")

    ads_result = diagnose_ads(ads_rows)
    search_result = mine_search_terms(search_rows)
    review_result = analyze_reviews(review_rows)
    listing_result = optimize_listing(listing, search_rows, review_result)
    creative_result = build_creative_brief(listing_result, review_result)

    report = build_weekly_report(
        {
            "ads": ads_result,
            "search_terms": search_result,
            "listing": listing_result,
            "reviews": review_result,
            "creative": creative_result,
        }
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return report


if __name__ == "__main__":
    run()
    print(f"Generated report: {DEFAULT_OUTPUT_PATH}")

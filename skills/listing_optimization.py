def _text_blob(listing):
    bullets = listing.get("bullets", [])
    return " ".join([listing.get("title", ""), *bullets]).lower()


def _normalize_terms(search_terms):
    terms = []
    for item in search_terms:
        if isinstance(item, dict):
            terms.append(item.get("term") or item.get("search_term") or "")
        else:
            terms.append(str(item))
    return [term.lower() for term in terms if term]


def optimize_listing(listing, search_terms, review_insights=None):
    review_insights = review_insights or {}
    body = _text_blob(listing)
    title = listing.get("title", "")
    bullets = listing.get("bullets", [])
    keywords = [kw.lower() for kw in listing.get("keywords", [])]
    mined_terms = _normalize_terms(search_terms)
    expected_terms = sorted(set(keywords + mined_terms))

    missing_terms = [term for term in expected_terms if term not in body]
    covered_terms = [term for term in expected_terms if term in body]
    risks = []
    recommendations = []

    if len(title) < 35:
        risks.append("Title underuses keyword space")
        recommendations.append("Expand the title with the main use case and core keyword.")
    if len(title) > 180:
        risks.append("Title may be too long")
    if float(listing.get("rating", 0) or 0) < 4.3:
        risks.append("Rating below trust threshold")
        recommendations.append("Use reviews and FAQ content to reduce conversion anxiety.")
    if len(bullets) < 5:
        risks.append("Bullet points are thin")
        recommendations.append("Add bullets for compatibility, speed, safety, and travel use.")
    if missing_terms:
        risks.append("Missing keyword coverage")
        recommendations.append(
            "Add missing buyer language: " + ", ".join(missing_terms[:5]) + "."
        )

    for pain in review_insights.get("pain_points", []):
        if pain not in body:
            recommendations.append(
                f"Address review pain point in copy or FAQ: {pain}."
            )

    return {
        "covered_terms": covered_terms,
        "missing_terms": missing_terms,
        "risks": risks or ["No major listing risk found"],
        "recommendations": list(dict.fromkeys(recommendations)),
    }

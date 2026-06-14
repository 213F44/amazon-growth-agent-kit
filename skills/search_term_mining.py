from skills.ads_diagnosis import safe_rate, to_float


def _term_record(row, reason, acos, cvr):
    return {
        "term": row.get("search_term", "unknown term"),
        "reason": reason,
        "spend": round(to_float(row.get("spend")), 2),
        "sales": round(to_float(row.get("sales")), 2),
        "orders": int(to_float(row.get("orders"))),
        "clicks": int(to_float(row.get("clicks"))),
        "acos": round(acos, 3),
        "cvr": round(cvr, 3),
    }


def mine_search_terms(rows):
    negative_candidates = []
    expansion_candidates = []
    watch_terms = []
    warnings = []

    for row in rows:
        spend = to_float(row.get("spend"))
        sales = to_float(row.get("sales"))
        orders = to_float(row.get("orders"))
        clicks = to_float(row.get("clicks"))
        acos = safe_rate(spend, sales)
        cvr = safe_rate(orders, clicks)

        if orders == 0 and spend >= 25:
            negative_candidates.append(
                _term_record(row, "Spend without orders", acos, cvr)
            )
        elif orders >= 2 and acos <= 0.25:
            expansion_candidates.append(
                _term_record(row, "Low ACOS with repeat orders", acos, cvr)
            )
        elif clicks >= 35 and cvr < 0.04:
            watch_terms.append(
                _term_record(row, "Traffic exists but conversion is weak", acos, cvr)
            )

    if not rows:
        warnings.append("No search term rows were provided.")

    return {
        "negative_candidates": negative_candidates,
        "expansion_candidates": expansion_candidates,
        "watch_terms": watch_terms,
        "warnings": warnings,
    }

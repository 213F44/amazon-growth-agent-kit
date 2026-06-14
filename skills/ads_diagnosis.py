def to_float(value, default=0.0):
    try:
        if value in (None, ""):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def safe_rate(numerator, denominator):
    if denominator == 0:
        return 0.0
    return numerator / denominator


def diagnose_ads(rows):
    campaigns = []
    total_spend = 0.0
    total_sales = 0.0
    total_clicks = 0.0
    total_orders = 0.0
    total_impressions = 0.0
    recommendations = []
    warnings = []

    for row in rows:
        spend = to_float(row.get("spend"))
        sales = to_float(row.get("sales"))
        clicks = to_float(row.get("clicks"))
        impressions = to_float(row.get("impressions"))
        orders = to_float(row.get("orders"))
        cpc = to_float(row.get("cpc"), safe_rate(spend, clicks))
        acos = safe_rate(spend, sales)
        ctr = safe_rate(clicks, impressions)
        cvr = safe_rate(orders, clicks)

        flags = []
        if acos >= 0.45 and spend >= 30:
            flags.append("High ACOS")
            recommendations.append(
                f"Reduce bids or isolate poor terms in {row.get('campaign', 'unknown campaign')}."
            )
        if spend >= 25 and orders <= 1:
            flags.append("Wasted spend risk")
            recommendations.append(
                f"Audit search terms and add negatives for {row.get('campaign', 'unknown campaign')}."
            )
        if ctr < 0.01 and impressions >= 1000:
            flags.append("Low CTR")
        if cvr < 0.04 and clicks >= 40:
            flags.append("Low CVR")
        if cpc >= 0.8:
            flags.append("High CPC")
        if orders >= 5 and acos <= 0.2:
            flags.append("Scale candidate")
            recommendations.append(
                f"Increase budget carefully for {row.get('campaign', 'unknown campaign')}."
            )

        campaigns.append(
            {
                "campaign": row.get("campaign", "Unnamed campaign"),
                "spend": round(spend, 2),
                "sales": round(sales, 2),
                "orders": int(orders),
                "acos": round(acos, 3),
                "ctr": round(ctr, 3),
                "cvr": round(cvr, 3),
                "cpc": round(cpc, 2),
                "flags": flags or ["Healthy"],
            }
        )

        total_spend += spend
        total_sales += sales
        total_clicks += clicks
        total_orders += orders
        total_impressions += impressions

    if not rows:
        warnings.append("No ad rows were provided.")

    summary = {
        "campaigns": len(rows),
        "total_spend": round(total_spend, 2),
        "total_sales": round(total_sales, 2),
        "total_orders": int(total_orders),
        "acos": round(safe_rate(total_spend, total_sales), 3),
        "ctr": round(safe_rate(total_clicks, total_impressions), 3),
        "cvr": round(safe_rate(total_orders, total_clicks), 3),
    }

    return {
        "summary": summary,
        "campaigns": campaigns,
        "recommendations": list(dict.fromkeys(recommendations)),
        "warnings": warnings,
    }

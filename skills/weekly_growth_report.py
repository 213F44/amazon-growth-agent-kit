def _bullet_list(items, empty_text="No items."):
    if not items:
        return f"- {empty_text}"
    return "\n".join(f"- {item}" for item in items)


def _format_campaign(campaign):
    flags = ", ".join(campaign["flags"])
    return (
        f"- {campaign['campaign']}: ACOS {campaign['acos']:.1%}, "
        f"CTR {campaign['ctr']:.1%}, CVR {campaign['cvr']:.1%}, flags: {flags}"
    )


def _format_term(record):
    return (
        f"- {record['term']}: {record['reason']} "
        f"(spend ${record['spend']}, ACOS {record['acos']:.1%}, CVR {record['cvr']:.1%})"
    )


def build_weekly_report(results):
    ads = results["ads"]
    terms = results["search_terms"]
    listing = results["listing"]
    reviews = results["reviews"]
    creative = results["creative"]

    campaigns = "\n".join(_format_campaign(row) for row in ads["campaigns"])
    negatives = "\n".join(_format_term(row) for row in terms["negative_candidates"])
    expansions = "\n".join(_format_term(row) for row in terms["expansion_candidates"])
    watch_terms = "\n".join(_format_term(row) for row in terms["watch_terms"])

    today = []
    today.extend(ads["recommendations"][:2])
    if terms["negative_candidates"]:
        today.append("Add negatives for spend-without-order search terms.")
    if listing["recommendations"]:
        today.append(listing["recommendations"][0])

    this_week = []
    if terms["expansion_candidates"]:
        this_week.append("Move low-ACOS converting terms into exact campaigns.")
    this_week.extend(creative["prompt_drafts"][:2])

    observe = []
    if terms["watch_terms"]:
        observe.append("Watch high-click low-CVR terms after Listing updates.")
    for risk in listing["risks"]:
        observe.append(f"Monitor Listing risk: {risk}.")

    return f"""# Amazon Growth Agent Report

> Demo note: all data in this report is simulated and desensitized for a job portfolio.

## Ads Diagnosis

Campaigns analyzed: {ads['summary']['campaigns']}

Overall ACOS: {ads['summary']['acos']:.1%}
Overall CTR: {ads['summary']['ctr']:.1%}
Overall CVR: {ads['summary']['cvr']:.1%}

{campaigns}

Recommendations:
{_bullet_list(ads['recommendations'], 'No immediate campaign actions.')}

## Search Term Mining

Negative candidates:
{negatives or '- No negative candidates.'}

Expansion candidates:
{expansions or '- No expansion candidates.'}

Watch terms:
{watch_terms or '- No watch terms.'}

## Listing Optimization

Covered terms: {', '.join(listing['covered_terms']) or 'None'}
Missing terms: {', '.join(listing['missing_terms']) or 'None'}

Risks:
{_bullet_list(listing['risks'])}

Recommendations:
{_bullet_list(listing['recommendations'], 'No listing recommendations.')}

## Review Insights

Positive themes: {', '.join(reviews['positive_themes']) or 'None'}
Pain points: {', '.join(reviews['pain_points']) or 'None'}

Creative angles:
{_bullet_list(reviews['creative_angles'], 'No creative angles.')}

FAQ ideas:
{_bullet_list(reviews['faq_ideas'], 'No FAQ ideas.')}

## Creative Brief

Main image brief:
{creative['main_image_brief']}

Lifestyle image brief:
{creative['lifestyle_image_brief']}

Short video script:
{_bullet_list(creative['short_video_script'])}

AI prompt drafts:
{_bullet_list(creative['prompt_drafts'])}

## Weekly Action Plan

Today:
{_bullet_list(today, 'No urgent actions.')}

This week:
{_bullet_list(this_week, 'No weekly actions.')}

Keep observing:
{_bullet_list(observe, 'No observation items.')}
"""

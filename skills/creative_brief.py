def _title_case_theme(theme):
    if theme == "fast charging":
        return "Fast charging"
    return theme.capitalize()


def build_creative_brief(listing_result, review_result, target_market="US"):
    themes = review_result.get("positive_themes", [])
    pains = review_result.get("pain_points", [])
    primary_theme = _title_case_theme(themes[0]) if themes else "Clear product benefit"
    primary_pain = pains[0] if pains else "buyer uncertainty"

    main_image_brief = (
        f"{primary_theme} hero image for {target_market}: show the product clearly, "
        "include device compatibility cues, and keep text minimal."
    )
    lifestyle_image_brief = (
        "Travel desk scene: charger in a backpack or airport workspace, with one phone "
        "and one laptop charging at the same time."
    )
    short_video_script = [
        "Hook: show a low-battery phone before leaving for a trip.",
        f"Proof: demonstrate {primary_theme.lower()} and compact travel use.",
        f"Trust: address {primary_pain} with a simple safety or usage note.",
    ]
    prompt_drafts = [
        "Generate a clean Amazon hero image for a compact 65W USB-C travel charger, white background, premium lighting.",
        "Generate a lifestyle image in an airport workspace showing a compact travel charger powering two devices.",
        "Generate a 15-second ecommerce video storyboard with problem, proof, and trust beats.",
    ]

    if listing_result.get("missing_terms"):
        prompt_drafts.append(
            "Include buyer language from keyword research: "
            + ", ".join(listing_result["missing_terms"][:3])
            + "."
        )

    return {
        "main_image_brief": main_image_brief,
        "lifestyle_image_brief": lifestyle_image_brief,
        "short_video_script": short_video_script,
        "prompt_drafts": prompt_drafts,
    }

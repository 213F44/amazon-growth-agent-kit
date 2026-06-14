THEME_KEYWORDS = {
    "fast charging": ["fast", "quick", "charging", "speed"],
    "compact": ["compact", "small", "portable", "travel"],
    "compatibility": ["compatible", "works with", "usb", "phone", "laptop"],
    "durability": ["durable", "solid", "sturdy", "reliable"],
}

PAIN_KEYWORDS = {
    "heat": ["hot", "heat", "warm", "overheat"],
    "instructions": ["instruction", "manual", "confusing", "unclear"],
    "packaging": ["package", "packaging", "box", "damaged"],
    "compatibility risk": ["not work", "incompatible", "failed"],
}


def _matches(text, words):
    lowered = text.lower()
    return any(word in lowered for word in words)


def analyze_reviews(rows):
    positive_themes = []
    pain_points = []
    creative_angles = []
    faq_ideas = []

    for row in rows:
        text = row.get("text", "")
        rating = float(row.get("rating", 0) or 0)

        if rating >= 4:
            for theme, words in THEME_KEYWORDS.items():
                if _matches(text, words) and theme not in positive_themes:
                    positive_themes.append(theme)
        if rating <= 3:
            for pain, words in PAIN_KEYWORDS.items():
                if _matches(text, words) and pain not in pain_points:
                    pain_points.append(pain)

    for theme in positive_themes:
        if theme == "fast charging":
            creative_angles.append("Show a phone and laptop charging before a flight.")
        elif theme == "compact":
            creative_angles.append("Show the charger fitting into a small travel pouch.")
        elif theme == "compatibility":
            creative_angles.append("Show multiple devices connected at a desk.")
        elif theme == "durability":
            creative_angles.append("Show premium materials and reinforced port details.")

    for pain in pain_points:
        if pain == "heat":
            faq_ideas.append("Explain normal warmth and safe-use charging conditions.")
        elif pain == "instructions":
            faq_ideas.append("Add a simple setup visual and port guide.")
        elif pain == "packaging":
            faq_ideas.append("Clarify package contents and protective packing.")
        elif pain == "compatibility risk":
            faq_ideas.append("List supported device types and charging limits.")

    return {
        "positive_themes": positive_themes,
        "pain_points": pain_points,
        "creative_angles": creative_angles,
        "faq_ideas": faq_ideas,
    }

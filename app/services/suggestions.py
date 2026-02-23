def generate_suggestions(lines):
    suggestions = []

    for line in lines:
        if len(line) > 80:
            suggestions.append("Line too long. Consider breaking it.")

    return suggestions
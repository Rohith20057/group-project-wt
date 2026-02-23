from app.services.tockenizer import tokenize
from app.services.patterns import explain_line
from app.services.error_detector import detect_errors
from app.services.suggestions import generate_suggestions
def analyze_code(code, language):
    lines = tokenize(code)

    explanations = []
    errors = detect_errors(lines)
    suggestions = generate_suggestions(lines)

    for line in lines:
        explanations.append(explain_line(line, language))

    return {
        "explanation": explanations,
        "errors": errors,
        "suggestions": suggestions
    }
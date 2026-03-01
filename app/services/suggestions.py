def generate_suggestions(lines):
    suggestions = []

    has_docstrings = False
    has_functions = False
    has_classes = False

    for i, line in enumerate(lines):
        line = line.strip()

        if line.startswith(("def ", "class ")):
            if "def" in line: has_functions = True
            if "class" in line: has_classes = True
                
        if '"""' in line or "'''" in line:
            has_docstrings = True

        if len(line) > 80:
            suggestions.append(f"Line {i+1} is too long ({len(line)} chars). Consider breaking it into multiple lines using backslash or parentheses.")

    if has_functions and not has_docstrings:
        suggestions.append("Consider adding docstrings to your functions to explain what they do.")

    return suggestions
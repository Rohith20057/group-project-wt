def explain_line(line, language):

    if line.startswith("def"):
        return "This line defines a function."

    elif line.startswith("for"):
        return "This line creates a loop that repeats for a sequence."

    elif line.startswith("while"):
        return "This line creates a loop that runs while a condition is true."

    elif line.startswith("if"):
        return "This line checks a condition."

    elif "=" in line and "==" not in line:
        return "This line assigns a value to a variable."

    elif "print" in line:
        return "This line prints output to the console."

    return "This line executes a statement."

def detect_errors(lines):
    errors = []

    for line in lines:
        if line.startswith("for") and ":" not in line:
            errors.append("Possible syntax error: missing ':' in for loop.")

        if line.startswith("if") and ":" not in line:
            errors.append("Possible syntax error: missing ':' in if condition.")

        if "==" in line and "=" in line and "if" not in line:
            errors.append("Check if you meant comparison (==) instead of assignment (=).")

    return errors

def greet():
    for i in range(5):
        print(i)

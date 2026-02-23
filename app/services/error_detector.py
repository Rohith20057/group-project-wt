def detect_errors(lines):
    errors = []

    for line in lines:
        if "==" in line and "=" in line and "if" not in line:
            errors.append("Possible assignment vs comparison mistake.")

    return errors
def detect_errors(lines):
    errors = []
    print("Hello")
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Missing colon checks
        if line.startswith(("for ", "if ", "while ", "def ", "class ")) and not line.endswith(":"):
            errors.append(f"Line {i+1}: Possible syntax error: missing ':' at end of line.")

        # Assignment vs equality check
        if "==" in line and "=" in line and "if" not in line and "while" not in line:
            errors.append(f"Line {i+1}: Check if you meant comparison (==) instead of assignment (=).")
            
        elif "=" in line and "if" in line and "==" not in line and "!=" not in line and ">=" not in line and "<=" not in line:
            errors.append(f"Line {i+1}: Possible assignment (=) inside an if condition. Did you mean comparison (==)?")

    return errors
def explain_line(line, language):

    line = line.strip()
    
    if not line:
        return "Empty line."

    if line.startswith("#") or line.startswith("//"):
        return "This is a comment."
        
    if line.startswith("import") or line.startswith("from"):
        return "This line imports external libraries or modules."

    if line.startswith("def") or line.startswith("function"):
        return "This line defines a new function."
        
    if line.startswith("class"):
        return "This line defines a new class."

    if line.startswith("for"):
        return "This line starts a 'for' loop to iterate over a sequence."

    if line.startswith("while"):
        return "This line starts a 'while' loop that continues as long as a condition is true."

    if line.startswith("if"):
        return "This line starts a conditional 'if' statement."
        
    if line.startswith("elif") or line.startswith("else if"):
        return "This line checks an alternative condition."
        
    if line.startswith("else"):
        return "This line handles the default case if the previous conditions were false."
        
    if line.startswith("return"):
        return "This line returns a value from the function."

    if "==" in line and "=" not in line.replace("==", ""):
        return "This line performs an equality check."
        
    if "=" in line and "==" not in line and "!=" not in line and ">=" not in line and "<=" not in line:
        return "This line assigns a value to a variable."

    if "print" in line or "console.log" in line:
        return "This line outputs information to the console."

    return "This line executes a statement or calls a function."


def tokenize(code: str):
    lines = code.split("\n")
    cleaned = [line.strip() for line in lines if line.strip()]
    return cleaned
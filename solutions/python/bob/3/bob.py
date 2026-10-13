def response(hey_bob):
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.rstrip().endswith("?"):
        return "Sure."
    elif hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!"
    return "Whatever."
def summarize_text(text, max_sentences=3):
    sentences = text.split(".")
    return ".".join(sentences[:max_sentences])

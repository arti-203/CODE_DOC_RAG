
def chunk_text(text, chunk_size=500):
    lines = text.split("\n")
    chunks = []
    current_chunk = []
    current_len = 0

    for line in lines:
        current_chunk.append(line)
        current_len += len(line)
        if current_len >= chunk_size:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_len = 0

    if current_chunk:
        chunks.append("\n".join(current_chunk))
    return chunks

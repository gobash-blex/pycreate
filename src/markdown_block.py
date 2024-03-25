def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in split_blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks
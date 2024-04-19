def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = []
    
    for block in raw_blocks:
        if block != "":
            blocks.append(block.strip())
    return blocks


markdown = """
# This is a heading



       This is a paragraph of text. It has some **bold** and *italic* words inside of it. 


   This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list item
* This is another list item
"""

blocks = markdown_to_blocks(markdown)
print(blocks)
print()
for block in blocks:
    print(block)
    print()


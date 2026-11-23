"""Six Words, One Story — make.fun entry.

The entry is the six-word story below; running this file prints it.
"""

STORY = "He bought flowers for her grave."

if __name__ == "__main__":
    words = STORY.split()
    assert len(words) == 6, f"the story must be exactly six words, got {len(words)}"
    print(STORY)

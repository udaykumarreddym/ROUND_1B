import fitz
from collections import defaultdict
import re

def is_heading(text):
    return (
        text.isupper()
        or text.endswith(":")
        or text.istitle()
        or bool(re.match(r"^\d+(\.\d+)*\s", text))
    )

def extract_sections(documents):
    sections = []

    for doc_name, doc in documents:
        for page_num, page in enumerate(doc):
            words = page.get_text("words")  # [[x0, y0, x1, y1, word, block, line, word_no]]
            if not words:
                continue

            # Group by y
            lines = defaultdict(list)
            for w in words:
                y = round(w[1], 1)
                lines[y].append(w)

            for y in sorted(lines):
                line = " ".join(w[4] for w in sorted(lines[y], key=lambda w: w[0])).strip()
                if len(line) < 10:
                    continue

                sections.append({
                    "document": doc_name,
                    "page": page_num,
                    "text": line,
                    "y": y,
                    "is_heading": is_heading(line)
                })

    return sections

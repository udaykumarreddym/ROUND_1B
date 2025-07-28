import json
from datetime import datetime

def format_output(input_meta, ranked_sections, output_path, target_similarity):
    output = {
        "metadata": {
            "input_documents": input_meta["documents"],
            "persona": input_meta["persona"],
            "job_to_be_done": input_meta["job_to_be_done"],
            "timestamp": str(datetime.now())
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    top_sections = ranked_sections[:5]

    for i, sec in enumerate(top_sections):
        output["extracted_sections"].append({
            "document": sec["document"],
            "section_title": sec["text"][:80].replace("\n", " "),
            "importance_rank": i + 1,
            "page_number": sec["page"]
        })

        # Subsection: next few lines on same page, sort by similarity closeness
        following_lines = [
            s for s in ranked_sections
            if s["document"] == sec["document"]
            and s["page"] == sec["page"]
            and s["y"] > sec["y"]
        ]

        if following_lines:
            best_sub = min(following_lines, key=lambda s: abs(s["score"] - target_similarity))
        else:
            best_sub = {"text": "No suitable subsection found."}

        output["subsection_analysis"].append({
            "document": sec["document"],
            "refined_text": best_sub["text"],
            "page_number": sec["page"]
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

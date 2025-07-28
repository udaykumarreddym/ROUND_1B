from app.loader import load_input, load_pdfs
from app.extractor import extract_sections
from app.embedder import get_model
from app.matcher import rank_sections
from app.formatter import format_output

def run_pipeline():
    input_data = load_input("data/input.json")
    documents = load_pdfs("data/pdfs")

    input_data["documents"] = [name for name, _ in documents]

    sections = extract_sections(documents)

    model = get_model()
    ranked_sections, target_similarity = rank_sections(
        sections,
        persona_text=input_data["persona"],
        job_text=input_data["job_to_be_done"],
        model=model
    )

    format_output(input_data, ranked_sections, "output/output.json", target_similarity)

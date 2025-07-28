# 🧠 ROUND_1B – MiniLink: Semantic Section Extraction from PDFs

## ✅ Solution Overview

MiniLink is a lightweight and fully offline system that semantically matches the most relevant sections and subsections from a set of PDF documents, given a user intent defined by a persona and a job-to-be-done.

This project was built to handle unstructured and layout-rich documents (e.g., guides, handbooks, reports) and produce a structured, ranked output with minimal resource requirements.

---

## 💡 Key Innovations

### 1. **Semantic Relevance Scoring with Alignment Calibration**

We use `all-MiniLM-L6-v2` (a compact Sentence-BERT model) to:

- Embed the **persona**
- Embed the **job-to-be-done**
- Embed every **line of text** extracted from PDFs
- Calculate a **target intent similarity score** between persona and job
- Rank each PDF line by **how close its similarity is to the target**, ensuring alignment with user needs

### 2. **Heading Detection with Layout-Aware Extraction**

- PDFs are parsed using **PyMuPDF** at word level.
- Words are **grouped into lines** based on vertical proximity.
- Headings are identified using formatting patterns like:
  - ALL CAPS
  - Numbered patterns (`1.2`, `2.3.1`)
  - Title Case
  - Ends with `:` (colon)

This enables us to detect **section boundaries** and treat them as candidates for ranking.

### 3. **Subsection Discovery Using Contextual Proximity**
- Once a top section is selected, the lines that **follow on the same page** are filtered.
- We select the **subsection text** that is **closest in semantic meaning to the persona–job intent**.
- This creates a natural, contextually linked **section–subsection pair**.

---

## 🧪 Output Format

We generate a single structured JSON with:

- Metadata:
  - List of input documents
  - Persona
  - Job-to-be-done
  - Timestamp
- Extracted Sections:
  - Top 5 ranked section titles with document name and page number
- Subsection Analysis:
  - Relevant follow-up text beneath each selected section

---

## ⚙️ How to Run

### ▶️ Run via Docker

```bash
docker build -t minilink-app .
docker run --rm -v $PWD/output:/app/output minilink-app
```

Input

JSON in data/input.json describing:

persona

job_to_be_done

list of PDFs

Output

Structured output in output/output.json

🧠 Why This Works

This solution balances:

Accuracy: Semantic intent matching instead of just keyword overlap

Robustness: Layout-aware parsing handles inconsistent PDF formatting

Efficiency: Fully offline (< 200MB model, < 10s runtime), no GPU needed

Generality: Works across any domain (travel, healthcare, technical, legal)

🙋 Author

Uday Kumar Reddy

Rukmangar

Web Alchemists

B.Tech CSE (Data Science)

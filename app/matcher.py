from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(sections, persona_text, job_text, model):
    query = f"{persona_text}. Task: {job_text}"
    section_texts = [s["text"] for s in sections]

    # Embed
    section_embeds = model.encode(section_texts, convert_to_tensor=True)
    query_embed = model.encode([query], convert_to_tensor=True)

    persona_embed = model.encode([persona_text], convert_to_tensor=True)
    job_embed = model.encode([job_text], convert_to_tensor=True)
    target_similarity = cosine_similarity(
        persona_embed.cpu().numpy(), job_embed.cpu().numpy()
    ).item()

    sims = cosine_similarity(query_embed.cpu().numpy(), section_embeds.cpu().numpy()).flatten()

    for i, s in enumerate(sections):
        s["score"] = float(sims[i])
        s["sim_distance"] = abs(sims[i] - target_similarity)

    # Headings + semantic closeness
    ranked = sorted(sections, key=lambda s: (not s["is_heading"], s["sim_distance"]))
    return ranked, target_similarity

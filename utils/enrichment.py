import spacy
from typing import Dict, Any

# נטען מודל אנגלי (אפשר להרחיב לעברית בהמשך)
nlp = spacy.load("en_core_web_sm")


def enrich_text(text: str) -> Dict[str, Any]:
    """
    העשרת טקסט: ישויות (NER), מילות מפתח (noun chunks), סיכום (משפט ראשון).
    מחזיר dict עם השדות: text, entities, keywords, summary
    """
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    keywords = list(
        {chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 2}
    )[:10]
    sents = list(doc.sents)
    summary = sents[0].text if sents else text[:120]
    return {
        "text": text,
        "entities": entities,
        "keywords": keywords,
        "summary": summary,
    }

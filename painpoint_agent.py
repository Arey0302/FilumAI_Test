import json
import re
from collections import Counter
from typing import List, Dict

# Load feature knowledge base
with open('features.json', encoding='utf-8') as f:
    FEATURES = json.load(f)

def preprocess(text: str) -> List[str]:
    # Lowercase, remove punctuation, split to words
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def match_features(pain_point: str, top_k: int = 3) -> List[Dict]:
    pain_words = set(preprocess(pain_point))
    scored = []
    for feat in FEATURES:
        # Gather all keywords and use_cases words
        keywords = set([k.lower() for k in feat.get('keywords', [])])
        use_case_words = set()
        for uc in feat.get('use_cases', []):
            use_case_words.update(preprocess(uc))
        # Count overlap
        overlap = len(pain_words & keywords) + len(pain_words & use_case_words)
        # Simple normalization
        max_possible = len(keywords) + len(use_case_words) or 1
        score = overlap / max_possible
        # Also check if any keyword appears as substring in pain_point
        for k in keywords:
            if k in pain_point.lower():
                score += 0.1
        scored.append((score, feat))
    # Sort by score desc
    scored.sort(reverse=True, key=lambda x: x[0])
    # Prepare output
    results = []
    for score, feat in scored[:top_k]:
        if score > 0:
            results.append({
                "feature_name": feat["feature_name"],
                "category": feat["category"],
                "description": feat["description"],
                "how_it_helps": feat["how_it_helps"],
                "relevance_score": round(float(score), 2)
            })
    return results

def main():
    print("Enter pain point (describe your business problem):")
    pain_point = input().strip()
    results = match_features(pain_point)
    print("\nRecommended solutions:")
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main() 
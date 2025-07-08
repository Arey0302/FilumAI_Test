# FilumAI Feature Search

This project provides a simple web interface to search for FilumAI features based on your business pain points or keywords.

## Features
- Input your pain point or keyword in natural language.
- The system suggests the most relevant FilumAI features.
- Results include feature name, description, how it helps, category, and relevance score.

## Requirements
- Python 3.8+
- pip

## Setup Instructions

1. **Clone or download this repository.**

2. **Create and activate a virtual environment (recommended):**

   - **On Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**

   ```bash
   pip install flask
   ```

4. **Run the application:**

   ```bash
   cd FilumAI
   python app.py
   ```

5. **Open your browser and go to:**

   ```
   http://localhost:5000
   ```

6. **Usage:**
- Enter your business pain point or keyword in the input box.
- Click "Search" to see the most relevant features.

## File Structure
- `app.py`: Flask web application.
- `features.json`: Feature knowledge base (English, editable).
- `painpoint_agent.py`: Logic for matching pain points to features.
- `templates/index.html`: Web interface template.

## Customization
- To add or edit features, modify `features.json`.
- To improve matching logic, edit `painpoint_agent.py`.

## Example Input/Output

Input: `We have trouble collecting customer feedback after purchase.`

Output:
```json
[
  {
    "feature_name": "Automated Post-Purchase Surveys",
    "category": "VoC - Surveys",
    "description": "...",
    "how_it_helps": "...",
    "relevance_score": 0.95
  }
]
```


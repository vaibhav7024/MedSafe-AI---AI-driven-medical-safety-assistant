
# 🛡️ MedSafe AI

**Your Intelligent Healthcare Assistant**

MedSafe AI is a modern, responsive web application built with Streamlit and powered by Google's Gemini Vision & LLM APIs. It is designed to act as a personal medical safety assistant, helping users understand their prescriptions, check for dangerous drug interactions, and get AI-guided advice on side effects—all within a beautiful, Apple-inspired mobile dashboard interface.

---

## ✨ Features

*   **💊 Medicine Interaction Checker**: Input multiple medications and let the advanced backend analyze known interactions, fuzzy-match active salts against our mock database, and generate patient-friendly AI guidance summaries for any identified risks. 
*   **📄 Prescription OCR Reader**: Say goodbye to unreadable doctor's handwriting. Upload a picture of a medical prescription and let Google's Generative AI Vision accurately extract the prescribed medicines and their active salts.
*   **🩺 Symptom & Doubt Solver**: Experiencing side effects from a new medication? Enter your symptoms and history to get instant educational guidance, home remedies, and an AI-driven emergency risk assessment predictor.
*   **📱 Immersive Mobile UI**: Designed from the ground up to feel like a premium native mobile application with custom CSS, Apple's San Francisco text typography, smooth hover transitions, and rounded pastel widgets.

## 🛠️ Technology Stack

*   **Frontend**: Python / [Streamlit](https://streamlit.io/)
*   **Styling**: Custom flex-box HTML and CSS 
*   **AI Engine**: [Google GenAI](https://pypi.org/project/google-generativeai/) (`gemini-2.5-flash`)
*   **Database Matching**: `thefuzz` for intelligent string grouping
*   **Image Processing**: `Pillow`

## 🚀 Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/Tusharsharma420/MedSafe-AI---AI-driven-medical-safety-assistant.git
cd MedSafe-AI---AI-driven-medical-safety-assistant
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. API Key Configuration
MedSafe AI heavily relies on Google's Gemini API for its intelligent features. You need to provide your own API key.

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `.env` in the root of the project directory.
3. Add the following line to the `.env` file:
```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Application
Start the Streamlit development server:
```bash
python -m streamlit run app.py
```
The application will open in your default browser at `http://localhost:8501`.

### 📂 Project Structure

c:/Vaibhav Jaiswal/medai/
├── 📄 app.py                         # Streamlit app router & global CSS entry
├── 📄 list_models.py                 # script to find exact Gemini model strings
├── 📄 requirements.txt               # Standard python dependency lock
├── 📁 data/
│   └── 📄 medicine_db.json           # Curated mock DB of drug salts & safety rules
├── 📁 utils/ 
│   ├── 📄 llm_helper.py              # GenerativeAI integrations and wrappers
│   ├── 📄 medicine_db.py             # Local DB parser & fuzzy matching logic
│   └── 📄 ocr_helper.py              # Image digestion and Vision API wrapper
└── 📁 views/ 
    ├── 📄 dashboard.py               # Main beautiful pastel dashboard home
    ├── 📄 interaction_checker.py     # Tool logic for checking safety
    ├── 📄 prescription_ocr.py        # Tool logic for scanning prescriptions
    └── 📄 symptom_solver.py          # Tool logic for generating medical guidance

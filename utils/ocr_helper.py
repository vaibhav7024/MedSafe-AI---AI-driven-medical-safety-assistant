import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Load env variables
load_dotenv()

# Configure Google Gen AI
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# We use gemini-2.5-flash for vision OCR (Pro exceeded free quota)
vision_model = genai.GenerativeModel('gemini-2.5-flash')

def extract_prescription_data(image_path):
    """
    Uses Gemini 1.5 Pro to extract medicine names from a prescription image and return them as JSON.
    """
    if not api_key:
        return {"error": "API Key not configured. Unable to process image."}
        
    prompt = """
    You are an expert pharmacist AI reading a prescription image (handwritten or printed).
    Extract the list of medicines prescribed from the image.
    For each medicine, extract or infer the 'name' and the probable 'active_salt' if you can determine it.
    
    Return exactly ONLY a JSON array of objects, with no markdown formatting or extra text.
    Example: 
    [
        {"name": "Aspirin 500mg", "active_salt": "Acetylsalicylic acid"},
        {"name": "SomeBrandName", "active_salt": "Somesaltname"}
    ]
    """
    try:
        # The image path is expected to be a local PIL image or path
        # In streamlit, it usually gives a BytesIO or PIL image
        import PIL.Image
        with PIL.Image.open(image_path) as img:
            response = vision_model.generate_content([prompt, img])
        text = response.text
        
        # Clean up in case the model returns markdown JSON blocks
        text = text.replace('```json', '').replace('```', '').strip()
        
        return json.loads(text)
    except Exception as e:
        return {"error": f"Error running OCR: {e}"}

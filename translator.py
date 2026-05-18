from google import genai
from google.genai import types as genai_types

from config import GEMINI_API_KEY, VERTEX_AI_PROJECT
from prompts import TRANSLATION_SYSTEM_INSTRUCTIONS

# --- API Setup ---
if VERTEX_AI_PROJECT:
    flex_mode = genai_types.HttpOptions(
        headers={
            "X-Vertex-AI-LLM-Request-Type": "shared",
            "X-Vertex-AI-LLM-Shared-Request-Type": "flex",
        }
    )
    client = genai.Client(
        vertexai=True, project=VERTEX_AI_PROJECT, http_options=flex_mode
    )
else:
    client = genai.Client(api_key=GEMINI_API_KEY)


def _get_model_config(temperature):
    safety_config = [
        genai_types.SafetySetting(
            category=genai_types.HarmCategory.HARM_CATEGORY_IMAGE_DANGEROUS_CONTENT,
            threshold=genai_types.HarmBlockThreshold.BLOCK_NONE,
        ),
        genai_types.SafetySetting(
            category=genai_types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=genai_types.HarmBlockThreshold.BLOCK_NONE,
        ),
        genai_types.SafetySetting(
            category=genai_types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=genai_types.HarmBlockThreshold.BLOCK_NONE,
        ),
        genai_types.SafetySetting(
            category=genai_types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=genai_types.HarmBlockThreshold.BLOCK_NONE,
        ),
    ]
    return genai_types.GenerateContentConfig(
        temperature=temperature,
        system_instruction=TRANSLATION_SYSTEM_INSTRUCTIONS,
        safety_settings=safety_config,
    )


def translate_batch_with_gemini(batch_prompt, model_name, temperature):
    """Calls the new Gemini API client with a single batch prompt."""
    model_config = _get_model_config(temperature)
    try:
        response = client.models.generate_content(
            model=model_name, contents=batch_prompt, config=model_config
        )
        if response and response.text:
            return response.text.strip()
        else:
            print("WARNING: No Response from the Gemini API for file")
            return ""
    except Exception as e:
        print(f"Error translating batch: {e}")
        return f"BATCH_TRANSLATION_ERROR: {e}"

import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types
from PIL import Image
import io
import json
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Gemini Client (uses GEMINI_API_KEY environment variable automatically)
client = genai.Client()

@app.post("/api/cook-ai")
async def cook_ai(file: UploadFile = File(...)):
    print("API Key loaded:", bool(os.getenv("GEMINI_API_KEY")))
    try:
        # Read the uploaded image file
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Prompt engineering to get structured JSON response
        prompt = """
        Analyze this image of kitchen ingredients. Identify the key items present, and generate a creative, delicious recipe using primarily these ingredients.
        Return ONLY a valid JSON object with the following keys:
        - "title": Name of the recipe (string)
        - "prepTime": Estimated cooking time (string, e.g., "20 mins")
        - "ingredients": List of detected/used ingredients (array of strings)
        - "steps": Step-by-step cooking instructions (array of strings)
        """

        # Call Gemini 2.5 Flash for multimodal vision task
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=[image, prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            ),
        )

        # Parse the JSON string returned by Gemini
        recipe_data = json.loads(response.text)
        return recipe_data

    except Exception as e:
        print("Error occurred:", str(e))
        raise HTTPException(status_code=500, detail=str.error(e) if hasattr(e, 'error') else str(e))
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# QuickChef AI 🍳✨

QuickChef AI is a modern full-stack web application that turns your random kitchen ingredients into delicious recipes instantly. Snap a photo of what’s in your fridge or pantry, and let Google Gemini’s multimodal vision capabilities analyze the ingredients and generate a step-by-step recipe on the fly.

## 🚀 Tech Stack

- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript (Responsive & Mobile-optimized camera interface)
- **Backend:** FastAPI (Python)
- **AI Engine:** Google Gemini SDK (`google-genai`), Multimodal Vision Model (`gemini-3.6-flash`)

---

## 📁 Project Structure

```text
quickchef-ai/
│
│── main.py          # FastAPI server & Gemini API integration
│── .env             # Environment variables (API keys)
└── index.html       # Single-page UI with camera capture & dynamic results
```

---

## 🛠️ Setup & Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/quickchef-ai.git
cd quickchef-ai
```

### 2. Backend Setup (FastAPI)
Navigate to your backend directory and install the required Python dependencies:

```bash
pip install fastapi uvicorn google-genai pillow python-multipart python-dotenv
```

Create a `.env` file in the root of your backend directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run the Backend Server
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload --port 8000
```
The server will run locally at `http://127.0.0.1:8000`.

### 4. Run the Frontend
Open the `index.html` file directly in any modern web browser or serve it using a local static server (like Live Server in VS Code).

---

## 💡 Usage Guide

1. Open the **QuickChef AI** web page on your phone or desktop.
2. Click the **"Open Camera & Snap"** button to capture an image of your ingredients (or upload an existing photo).
3. Review the image preview and hit **"Generate Recipe with AI"**.
4. The backend securely sends the image to Gemini, parses the returned JSON structure, and instantly displays the recipe title, cooking time, detected ingredient tags, and step-by-step instructions.

---

## 🛡️ Security Note
Your Gemini API key remains secure on the FastAPI backend and is never exposed to the frontend client.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
# 🌐 Language & Sentiment Analyzer

This project is a **full-stack NLP tool** that detects the **language**, analyzes **sentiment**, and evaluates **toxicity** of a given text.  

It consists of:
- 🐍 **Backend**: FastAPI (Python) for NLP pipelines  
- ⚛️ **Frontend**: React + TailwindCSS + Recharts for visualization  

---

## 🚀 Features
- **Language Detection** – Identify the language with confidence score.  
- **Sentiment Analysis** – Classify text as `positive`, `neutral`, or `negative`.  
- **Toxicity Detection** – Detect harmful or toxic language.  
- **Interactive Dashboard** – Visualize results with **Bar charts** (language confidence) and **Pie charts** (sentiment).  
- **AI Assistant UI** – Friendly robot-girl avatar for fun interactions.  

---

## 🖼️ Screenshots
Here are some previews of the app (stored in the `public/` folder of this repo):  

### Home Screen  
![Home Screen](public/screenshot1.jpg)

### Analysis Results  
![Analysis Results](public/screenshot2.png)  

*(Replace `screenshot1.png` / `screenshot2.png` with the actual file names in your `public/` folder.)*

---

## ⚙️ Installation & Setup

### Backend (FastAPI)
1. Navigate to backend folder:
   ```bash
   cd backend
2. Create a virtual environment & install dependencies:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

```
3. Run the server:
```
uvicorn main:app --reload

```
4. FastAPI will run at:
👉 http://127.0.0.1:8000

# Frontend (React)

1. Navigate to frontend folder:

```cd frontend

```
2. Install dependencies:
```
npm install

```
3. Start the React app:
```
npm run dev
```

Frontend will run at:
👉 http://localhost:5173 (or similar Vite port)

📊 Example Usage

Enter text into the input box (e.g., "Bonjour, je suis heureux aujourd'hui!").

Click Analyze.

You’ll see:

🌐 Language: French (98.5%)

😊 Sentiment: Positive (pie chart visualization)

⚠️ Toxicity: Non-toxic (2.3%)

🤝 Contributions

We welcome contributions to improve this project!
You can contribute by:

🐛 Fixing bugs

🌍 Adding new language models

🎨 Improving UI/UX

Please refer to the CONTRIBUTING.md
 (if available) for guidelines.

📜 License

This project is licensed under the MIT License.
See LICENSE
 for details.

✨ Enjoy exploring languages, sentiments, and toxicity with your AI Assistant!

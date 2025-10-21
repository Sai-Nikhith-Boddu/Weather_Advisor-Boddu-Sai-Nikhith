# 🌤️ Weather Advisor

A Flask-based AI Weather Assistant that provides natural, human-like weather responses using the **Ollama Llama 3 model**, and also displays temperature and precipitation visualizations.  
The app combines a conversational chatbot and a weather dashboard interface.

---

## 🚀 Features
- AI-powered weather assistant with natural responses
- Dashboard visualization (temperature & precipitation)
- Forecast data for today or next 3 days
- Built using Flask, Chart.js, and the wttr.in API
- Supports conversation-style UI with chat history

---

## 🧠 Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **AI Model:** Ollama (Llama 3)
- **Visualization:** Chart.js
- **API:** wttr.in (Weather data source)

---

## 📂 Project Structure
Weather_Advisor/
│
├── ai-conversations/
│
├── Resources/
│ ├── app.py
│ ├── weather_advisor.py
│ └── templates/
│ └── index.html
│
├── .gitignore
├── README.md
├── reflection.md
├── checklist.md
└── requirements.txt

▶️ Run the App
python Resources/app.py
Then open http://127.0.0.1:5000
 in your browser.

 🧭 AI and Ethics

This project follows Michael Brock’s AI-Conversations Framework, emphasizing:

Transparency in AI-generated content

Awareness of model limitations (Ollama Llama3)

Ethical handling of user data (no storage or profiling)

Clear distinction between human and AI-generated responses

💬 Example Conversations

“Do I need an umbrella today in Perth?”

“What’s the weather like in Sydney tomorrow?”

“Is it hot outside in Melbourne?”

“Will it rain this weekend in Adelaide?”

“How cold is it in Canberra right now?”

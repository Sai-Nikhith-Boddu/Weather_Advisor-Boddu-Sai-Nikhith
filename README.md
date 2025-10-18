# 🌦️ Weather Advisor

An AI-powered weather assistant that combines real-time weather data with conversational AI to provide human-like weather insights.  
Users can ask natural questions such as *“Do I need an umbrella today in Sydney?”* or *“Is it cold tomorrow in Perth?”*, and the system responds naturally with forecasts and advice.  
This project demonstrates intentional AI prompting, data visualisation, and full-stack integration.

---

## 🌤️ Features

- 🤖 **AI Chatbot** — answers user questions using **Ollama’s LLaMA3** model.  
- ☁️ **Live Weather Data** — sourced from the free [wttr.in](https://wttr.in) API.  
- 📊 **Visual Dashboard** — temperature, humidity, and precipitation charts using **Chart.js**.  
- 💬 **Conversational Interface** — logs previous chat history.  
- 🔒 **Error-Handling** — gracefully manages API or network failures.  
- 🧠 **AI Documentation** — all AI prompts and reflections are saved in the `ai-conversations/` folder.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML, CSS, JavaScript |
| **AI Model** | Ollama (LLaMA3) |
| **Weather Data** | wttr.in API |
| **Visualisation** | Chart.js |
| **Version Control** | Git & GitHub |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sai-Nikhith-Boddu/Weather_Advisor-Boddu-Sai-Nikhith.git
cd Weather_Advisor-Boddu-Sai-Nikhith

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure AI and Weather API
ollama pull llama3
Make sure Ollama
 is installed on your system.
The app uses the free wttr.in API for real-time weather — no API key is required.

4️⃣ Run the Application
flask run
Then open your browser and go to:
👉 http://localhost:5000

🗂️ Project Structure
Weather_Advisor/
│
├── ai-conversations/             # AI prompting documentation (5 logs + summary)
│   ├── Conversation1.txt
│   ├── Conversation2.txt
│   ├── Conversation3.txt
│   ├── Conversation4.txt
│   ├── Conversation5.txt
│   
│
├── static/                       # CSS, JS, and image files
├── templates/                    # HTML templates for Flask views
├── weather_data.py               # Fetches and structures weather data
├── weather_advisor.py            # Main Flask application and AI integration
├── requirements.txt              # Python dependencies
├── submission/                   # Reflection and submission checklist
└── README.md                     # Project documentation (this file)

🤖 AI Conversations & Prompting Log

This project was developed following intentional prompting principles.
All AI interactions are documented inside the ai-conversations/
 folder.

Each file includes:

The prompt provided to the AI model

The AI-generated code or explanation

The before-and-after implementation changes

A short reflection describing what was learned

These logs show transparency, accountability, and responsible AI usage — fully aligned with the Weatherwise Template


🧾 Submission & Reflection

A comprehensive reflection on the development journey is included in the submission/
 folder.
This document outlines:

The role of AI tools in coding, debugging, and design

Key challenges faced and how they were resolved

Insights gained from using AI ethically and effectively in software development

🪪 License & Acknowledgements

Developed by Sai-Nikhith Boddu as part of the Weatherwise project coursework.

Acknowledgements

Flask
 — backend web framework

Ollama
 — local AI model runtime (LLaMA3)

wttr.in
 — weather data provider

Chart.js
 — data visualisation library

Michael Borck’s Weatherwise Template
 — structural and academic reference

## 📬 Contact

For feedback or contributions, open an issue or reach out via GitHub:  
**[Sai-Nikhith Boddu](https://github.com/Sai-Nikhith-Boddu)**


---

### ✅ Notes to make it render perfectly
1. **Blank line before every ```bash and after every ```**.  
   - If even one is missing, GitHub treats the rest of your text as part of the code block.  
2. Keep the `## ⚙️ Installation & Setup` heading on its own line, with one empty line below it.  
3. Make sure there’s **no extra indentation** (no spaces before ```bash).  

---

To verify:
1. Paste this section into your README.  
2. Click **Preview** in GitHub’s editor — you should now see each step in its own neat grey box.  

---

Would you like me to resend your **entire README.md** with these fixed blank lines included everywhere (so everything renders 100 % correctly on GitHub)?


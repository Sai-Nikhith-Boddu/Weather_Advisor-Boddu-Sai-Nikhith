# Weather Advisor  

Weather Advisor is an AI-powered web application built with Flask and Ollama that provides natural language weather insights.  
Users can ask questions such as *“Do I need an umbrella today in Sydney?”* and receive human-like answers, along with a weather dashboard showing temperature, humidity, and precipitation charts.

## 🌤️ Features
- AI Chatbot using LLaMA3 via Ollama.
- Real-time weather data from wttr.in.
- Visual weather charts with Chart.js.
- User-friendly Flask web interface.
- AI prompting documentation in `ai-conversations/`.

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sai-Nikhith-Boddu/Weather_Advisor-Boddu-Sai-Nikhith.git
cd Weather_Advisor-Boddu-Sai-Nikhith

pip install -r requirements.txt

ollama pull llama3

flask run


---

### 🗂️ Project Structure

```markdown
## 🗂️ Project Structure


## 🤖 AI Conversations & Prompting Log

This project was developed using **intentional AI prompting** practices.  
All AI prompts, generated code, and reflections are saved in the [`ai-conversations/`](./ai-conversations/) folder.

Each file includes:
- The **prompt** given to AI.
- The **AI’s code response**.
- **Before & after changes** in implementation.
- A short **reflection** describing how AI guidance was applied.

These demonstrate responsible and transparent use of AI in software development, in line with the [Weatherwise Template](https://github.com/michaelborck-curtin/weatherwise-template).

## 🧾 Submission & Reflection

A detailed reflection on the development process and AI usage is included in the [`submission/`](./submission/) folder.  
This covers:
- Learning outcomes and challenges faced.
- How AI assistance improved productivity.
- Ethical considerations and transparency in AI usage.

## 🪪 License & Acknowledgements

Developed by **Sai-Nikhith Boddu** as part of the Weatherwise project coursework.

Special thanks to:
- [Flask](https://flask.palletsprojects.com/) — web framework  
- [Ollama](https://ollama.com) — AI model runtime (LLaMA3)  
- [wttr.in](https://wttr.in) — Weather data provider  
- [Chart.js](https://www.chartjs.org) — Data visualisation  
- [Michael Borck’s Weatherwise Template](https://github.com/michaelborck-curtin/weatherwise-template) — for project structure and academic guidance

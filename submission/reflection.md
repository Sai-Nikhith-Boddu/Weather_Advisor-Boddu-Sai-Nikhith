# Reflection – AI Weather Advisor Project

## Project Overview
This project integrates Artificial Intelligence (AI) with real-time weather data to create an interactive **Weather Advisor Web Application**. The system uses **Flask** for backend services, **HTML/CSS/JS** for the frontend interface, and **Ollama (Llama 3)** for generating human-like weather responses. Users can either chat with the AI chatbot or view temperature and precipitation visualizations in the Weather Dashboard.

---

## Development Process
The development began with creating a Python backend using **Flask** to manage user requests, weather data fetching, and AI-generated responses. The **wttr.in API** was used to collect weather data, while the **Ollama Llama 3 model** produced conversational responses.

On the frontend, **HTML and JavaScript** were used to build a clean, tab-based interface with two sections:  
1. **Chatbot:** A conversational weather assistant that provides natural language responses.  
2. **Dashboard:** A visualization panel displaying weather trends through **Chart.js** graphs.

---

## Key Learnings
- Gained a deeper understanding of **Flask routing**, RESTful APIs, and integration with AI language models.  
- Learned to manage front-end and back-end communication using **AJAX and JSON**.  
- Explored **data visualization techniques** to display temperature and precipitation trends effectively.  
- Improved debugging skills, especially in resolving server and API connectivity errors.

---

## Challenges Faced
- Encountered memory issues when running Ollama models locally; resolved by switching to a lighter version.
- Had to fix errors in visualizations where incorrect graph data appeared in both dashboard and chatbot tabs.
- Managed file structure alignment between Flask templates and static assets to ensure smooth GitHub deployment.

---

## Future Enhancements
- Implement **user authentication** and session-based weather history.
- Deploy the app to a cloud service such as **Render** or **Heroku**.
- Add **speech-to-text** functionality for more natural interaction.
- Expand AI capabilities for forecasting and lifestyle recommendations (e.g., “Is it good weather for running?”).

---

## Reflection Summary
Overall, this project enhanced my understanding of **AI-powered web development** and the importance of structured design between backend logic and frontend presentation. Integrating Flask, Ollama, and visualization tools created a robust learning experience in building intelligent, data-driven systems.

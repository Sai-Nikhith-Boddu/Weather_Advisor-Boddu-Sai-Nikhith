from flask import Flask, render_template, request, jsonify
import requests, json, ollama, re

app = Flask(__name__)

# ------------------ GLOBAL CHAT HISTORY ------------------ #
chat_history = []

# ---------------- WEATHER DATA FETCH ---------------- #

def get_weather_data(location):
    """Fetch weather data for a given location using wttr.in API."""
    url = f"https://wttr.in/{location}?format=j1"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# ---------------- PARSE QUESTION WITH OLLAMA3 ---------------- #

def parse_question_with_ai(question):
    """Use Ollama3 to extract structured info from user query."""
    prompt = (
        "Extract the location, time period, and weather attribute from the following weather question. "
        "Return ONLY a JSON object with keys: location, time_period, and attribute. "
        "If not mentioned, assume time_period='today' and attribute='weather'.\n\n"
        f"Question: {question}\nJSON:"
    )
    try:
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        print(f"⚠️ Ollama parse error: {e}")
        return None

def extract_json(text):
    """Extract JSON object safely from AI output."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return None
    return None

# ---------------- GENERATE HUMANIZED RESPONSE ---------------- #

def generate_human_response(weather_data, question, location):
    """Use Ollama3 to generate a human-like, short weather response."""
    current = weather_data["current_condition"][0]
    desc = current["weatherDesc"][0]["value"]
    temp = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    precip = current["precipMM"]
    humidity = current["humidity"]
    wind = current["windspeedKmph"]

    today_summary = (
        f"The current weather in {location.title()} is {desc.lower()} with a temperature of {temp}°C "
        f"(feels like {feels_like}°C), humidity {humidity}%, and precipitation of {precip} mm. "
        f"Wind speed is around {wind} km/h."
    )

    prompt = (
        "You are a friendly weather assistant. "
        "Using the given current weather data and the user's question, respond in one short, natural human sentence. "
        "Do not show numerical values or forecasts. Be conversational and direct.\n\n"
        "If the question is about umbrellas or raincoats, decide based on precipitation or rain description. "
        "If it's about temperature, mention if it's warm, cold, or pleasant.\n\n"
        f"Current weather data: {today_summary}\n"
        f"User question: {question}\n\n"
        "Example responses:\n"
        "- 'Yes, you’ll probably need an umbrella — it looks rainy today.'\n"
        "- 'No, it’s sunny and clear — no umbrella needed.'\n"
        "- 'It’s warm and pleasant outside — perfect weather!'\n"
        "- 'Looks cloudy but dry — you should be fine without a raincoat.'\n\n"
        "Now reply naturally in one or two short sentences:"
    )

    try:
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Ollama error: {e}"

# ---------------- ROUTES ---------------- #

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Handle chatbot queries and maintain conversation history."""
    global chat_history
    data = request.get_json()
    question = data.get("question", "").strip()
    if not question:
        chat_history.append({"sender": "ai", "text": "Please enter a question."})
        return jsonify({"chat": chat_history})

    chat_history.append({"sender": "user", "text": question})

    parsed = parse_question_with_ai(question)
    info = extract_json(parsed) if parsed else None
    location = info.get("location", "Perth") if info else "Perth"

    try:
        weather_data = get_weather_data(location)
        ai_response = generate_human_response(weather_data, question, location)

        if not ai_response or "⚠️" in ai_response:
            ai_response = "Sorry, I couldn’t generate a valid response right now."

        chat_history.append({"sender": "ai", "text": ai_response})
        return jsonify({"chat": chat_history})
    except Exception as e:
        error_msg = f"⚠️ Server error: {str(e)}"
        chat_history.append({"sender": "ai", "text": error_msg})
        return jsonify({"chat": chat_history})

@app.route("/dashboard", methods=["POST"])
def dashboard():
    """Dashboard route — provides data for temperature & precipitation visualizations."""
    data = request.get_json()
    location = data.get("location", "Perth")
    time_period = data.get("timePeriod", "today")

    weather_data = get_weather_data(location)

    if time_period == "today":
        dates = ["Today"]
        temps = [int(weather_data["current_condition"][0]["temp_C"])]
        precips = [float(weather_data["current_condition"][0]["precipMM"])]
    else:
        dates = [d["date"] for d in weather_data["weather"][:3]]
        temps = [int(d["avgtempC"]) for d in weather_data["weather"][:3]]
        precips = [sum(float(h["precipMM"]) for h in d["hourly"]) / len(d["hourly"]) for d in weather_data["weather"][:3]]

    return jsonify({
        "dates": dates,
        "temps": temps,
        "precips": precips
    })

if __name__ == "__main__":
    app.run(debug=True)


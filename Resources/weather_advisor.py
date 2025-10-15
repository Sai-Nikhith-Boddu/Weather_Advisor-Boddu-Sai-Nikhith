import requests
import json
import ollama
import re
import matplotlib.pyplot as plt

# ---------------- WEATHER DATA FETCH ---------------- #

def get_weather_data(location):
    """Fetch weather data for a given location using wttr.in API."""
    try:
        url = f"https://wttr.in/{location}?format=j1"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Failed to fetch weather data: {e}"}

# ---------------- PARSE QUESTION WITH OLLAMA3 ---------------- #

def parse_question_with_ai(question):
    """Use Ollama3 to extract structured info from user query."""
    prompt = (
        "Extract weather details from the question below. "
        "Return ONLY a JSON object with keys: location, time_period, and attribute. "
        "If not mentioned, set time_period='today' and attribute='weather'.\n\n"
        f"Question: {question}\nJSON:"
    )

    try:
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        print(f"⚠️ Error calling Ollama: {e}")
        return None

def extract_json(text):
    """Extract JSON object safely from AI output."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return None

# ---------------- GENERATE HUMANIZED RESPONSE ---------------- #

def generate_human_response(weather_data, question, location):
    """Use Ollama3 to generate a human-like weather reply."""
    if "error" in weather_data:
        return weather_data["error"]

    current = weather_data["current_condition"][0]
    desc = current["weatherDesc"][0]["value"]
    temp = current["temp_C"]
    precip = current["precipMM"]
    humidity = current["humidity"]

    weather_summary = (
        f"In {location.title()}, it's currently {desc.lower()} with {temp}°C temperature, "
        f"humidity {humidity}%, and {precip} mm precipitation."
    )

    prompt = (
        "You are a helpful and friendly weather assistant. "
        "Using the given weather data and the user's question, respond in a short, natural human tone. "
        "If the question is about umbrella or raincoat, decide based on rain/precipitation data. "
        "Be concise and conversational.\n\n"
        f"Weather data: {weather_summary}\n"
        f"User question: {question}\n\n"
        "Example responses:\n"
        "- 'Yes, please take an umbrella — it’s likely to rain today.'\n"
        "- 'No, it’s clear and sunny — no umbrella needed.'\n"
        "- 'It’s cloudy but not rainy — maybe keep a raincoat handy just in case.'\n\n"
        "Now respond naturally:"
    )

    try:
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Ollama error: {e}"

# ---------------- VISUALIZATION FUNCTIONS ---------------- #

def visualize_temperature_forecast(weather_data, location):
    """Plot temperature forecast for next 3 days."""
    days = weather_data["weather"][:3]
    dates = [d["date"] for d in days]
    avg_temps = [int(d["avgtempC"]) for d in days]

    plt.figure(figsize=(6, 4))
    plt.plot(dates, avg_temps, marker='o', color='orange', label='Avg Temperature (°C)')
    plt.title(f"Temperature Forecast - {location.title()}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def visualize_precipitation_forecast(weather_data, location):
    """Plot precipitation forecast for next 3 days."""
    days = weather_data["weather"][:3]
    dates = [d["date"] for d in days]
    avg_precip = []

    for day in days:
        hourly = day["hourly"]
        total_precip = sum(float(h["precipMM"]) for h in hourly)
        avg_precip.append(round(total_precip / len(hourly), 2))

    plt.figure(figsize=(6, 4))
    plt.bar(dates, avg_precip, color='skyblue', edgecolor='black')
    plt.title(f"Precipitation Forecast - {location.title()}")
    plt.xlabel("Date")
    plt.ylabel("Avg Precipitation (mm)")
    plt.tight_layout()
    plt.show()

# ---------------- MAIN FUNCTION ---------------- #

def get_weather_response(question):
    """Main function to handle user question and return AI-generated answer."""
    parsed = parse_question_with_ai(question)
    if not parsed:
        return None, "Sorry, I couldn’t understand your question."

    info = extract_json(parsed)
    if not info:
        return None, "Sorry, I couldn’t extract valid details."

    location = info.get("location", "Perth").strip() or "Perth"
    weather_data = get_weather_data(location)
    ai_response = generate_human_response(weather_data, question, location)

    return weather_data, ai_response

# ---------------- RUN THE ASSISTANT ---------------- #

if __name__ == "__main__":
    print("🌦️ Weather Assistant — powered by Ollama 3")
    print("Type your question (e.g., 'Do I need a raincoat today in Hyderabad?')\n")

    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Stay safe!")
            break

        weather_data, answer = get_weather_response(question)
        print(f"\n🤖 Assistant: {answer}\n")

        if weather_data:
            print("Would you like to see a visualization?")
            print("1️⃣ Temperature Forecast\n2️⃣ Precipitation Forecast\n3️⃣ Skip")
            choice = input("Enter choice (1/2/3): ").strip()

            if choice == "1":
                visualize_temperature_forecast(weather_data, weather_data["nearest_area"][0]["areaName"][0]["value"])
            elif choice == "2":
                visualize_precipitation_forecast(weather_data, weather_data["nearest_area"][0]["areaName"][0]["value"])
            else:
                print("✅ Skipping visualization.\n")


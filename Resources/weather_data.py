"""
weather_data.py
---------------
Handles weather data operations for the AI Weather Assistant.
Fetches live weather data, interprets user questions, and generates
natural conversational responses via Ollama (LLaMA 3).
"""

import requests
import json
import ollama
import re


# ---------------- WEATHER DATA FETCH ---------------- #

def get_weather_data(location):
    """Fetch live weather data for a given location from wttr.in API."""
    try:
        url = f"https://wttr.in/{location}?format=j1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ Weather fetch error: {e}")
        return {"error": f"Failed to fetch weather data: {e}"}


# ---------------- AI QUESTION PARSING ---------------- #

def parse_question_with_ai(question):
    """
    Parse user's question to extract location, time, and attribute.
    Uses Ollama to understand the query.
    """
    prompt = (
        "Extract the location, time period, and weather attribute from the question below. "
        "Return ONLY a JSON object with keys: location, time_period, and attribute. "
        "If something is missing, use defaults: location='Perth', time_period='today', attribute='weather'.\n\n"
        f"Question: {question}\nJSON:"
    )

    try:
        raw = ollama.chat(model="llama3:instruct", messages=[{"role": "user", "content": prompt}])
        # Handle different Ollama return formats
        if isinstance(raw, str):
            return raw
        if isinstance(raw, dict):
            if "message" in raw and "content" in raw["message"]:
                return raw["message"]["content"]
            if "messages" in raw and isinstance(raw["messages"], list):
                for msg in raw["messages"]:
                    if "content" in msg:
                        return msg["content"]
        return json.dumps({"location": "Perth", "time_period": "today", "attribute": "weather"})
    except Exception as e:
        print(f"⚠️ Ollama parsing error: {e}")
        return json.dumps({"location": "Perth", "time_period": "today", "attribute": "weather"})


def extract_json(text):
    """Extract JSON safely from AI output text."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return None


# ---------------- HUMANIZED WEATHER RESPONSE ---------------- #

def generate_human_response(weather_data, question, location):
    """
    Generate a short, conversational weather response using Ollama.
    Returns safe, human-like fallback if AI or data fails.
    """
    if not weather_data or "error" in weather_data:
        return weather_data.get("error", "⚠️ Unable to retrieve weather data.")

    try:
        current = weather_data["current_condition"][0]
        desc = current.get("weatherDesc", [{}])[0].get("value", "unknown")
        temp = current.get("temp_C", "N/A")
        feels_like = current.get("FeelsLikeC", "N/A")
        precip = current.get("precipMM", "N/A")
        humidity = current.get("humidity", "N/A")
        wind = current.get("windspeedKmph", "N/A")

        summary = (
            f"The weather in {location.title()} is currently {desc.lower()}, "
            f"with {temp}°C temperature (feels like {feels_like}°C), "
            f"humidity {humidity}%, wind speed {wind} km/h, "
            f"and precipitation {precip} mm."
        )

        prompt = (
            "You are a kind and friendly weather assistant. "
            "Use the following weather summary to respond to the user's question naturally.\n\n"
            f"Weather summary: {summary}\n"
            f"User question: {question}\n\n"
            "Guidelines:\n"
            "- Keep it under 3 short sentences.\n"
            "- Use a natural, human tone.\n"
            "- If precipitation > 0, suggest an umbrella.\n"
            "- If temperature < 15°C, suggest a jacket.\n"
            "- Avoid giving raw numbers in your answer.\n"
            "- Never mention that you are an AI.\n"
            "Now write your response:"
        )

        raw = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])

        # Debugging print — see what Ollama actually returned
        print("\n🔍 Raw Ollama output:\n", raw, "\n---------------------\n")

        # Handle all possible formats
        if isinstance(raw, str):
            return raw.strip()

        if isinstance(raw, dict):
            if "message" in raw and "content" in raw["message"]:
                return raw["message"]["content"].strip()
            if "messages" in raw and isinstance(raw["messages"], list):
                for msg in raw["messages"]:
                    if isinstance(msg, dict) and "content" in msg:
                        return msg["content"].strip()
            # fallback: join any string values found
            for v in raw.values():
                if isinstance(v, str) and v.strip():
                    return v.strip()

        # last fallback
        return "It seems to be a normal day — nothing unusual with the weather!"

    except Exception as e:
        print(f"⚠️ Ollama generation error: {e}")
        return "Sorry, I couldn’t generate a valid response right now. Please try again later."


# ---------------- FORECAST DATA FOR VISUALIZATION ---------------- #

def prepare_visual_data(weather_data, time_period="today"):
    """Prepare temperature and precipitation data for dashboard charts."""
    try:
        if time_period == "today":
            dates = ["Today"]
            temps = [int(weather_data["current_condition"][0]["temp_C"])]
            precips = [float(weather_data["current_condition"][0]["precipMM"])]
        else:
            dates = [d["date"] for d in weather_data["weather"][:3]]
            temps = [int(d["avgtempC"]) for d in weather_data["weather"][:3]]
            precips = [
                round(
                    sum(float(h.get("precipMM", 0)) for h in d["hourly"]) / len(d["hourly"]), 2
                )
                for d in weather_data["weather"][:3]
            ]

        return {"dates": dates, "temps": temps, "precips": precips}
    except Exception as e:
        print(f"⚠️ Data formatting error: {e}")
        return {"error": f"Failed to prepare visualization data: {e}"}


# ---------------- MAIN FUNCTION (LOCAL TEST) ---------------- #

if __name__ == "__main__":
    print("🌦️ Weather Assistant — Local Test Mode")
    user_question = input("Ask something (e.g., Do I need an umbrella today in Sydney?): ")

    parsed = parse_question_with_ai(user_question)
    info = extract_json(parsed) if parsed else None
    location = (info.get("location") if info else None) or "Perth"

    weather = get_weather_data(location)
    answer = generate_human_response(weather, user_question, location)

    print("\n🤖 AI Response:\n", answer)

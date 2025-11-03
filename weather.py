import streamlit as st
import requests
import pandas as pd
import pydeck as pdk
from datetime import datetime

st.set_page_config(page_title="🌤️ Smart Weather + Map Advisor", layout="wide")
st.title("🌤️ Smart Weather + Map Advisor")
st.caption("Live weather, smart advice, and interactive map — IP-based detection, no JS required.")

# --- Detect location ---
lat = lon = None
city = "Unknown"

try:
    location_data = requests.get("https://ipapi.co/json/", timeout=5).json()
    lat = float(location_data.get("latitude", 17.385))
    lon = float(location_data.get("longitude", 78.486))
    city = location_data.get("city", "Unknown")
    st.success(f"Approximate location from IP: {city} (Lat: {lat}, Lon: {lon})")
except Exception:
    st.warning("Could not detect location via IP. Please enter manually.")

lat = st.number_input("Latitude:", value=lat if lat else 17.385)
lon = st.number_input("Longitude:", value=lon if lon else 78.486)
city_input = st.text_input("City name (optional):", value=city)

# --- Weather API ---
API_KEY = "98c4c53a9dbd06ec77bbc029cd164faa"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

try:
    response = requests.get(weather_url, timeout=10).json()
except Exception as e:
    st.error(f"Unable to fetch weather: {e}")
    st.stop()

if response.get("cod") == 200:
    name = response.get("name") or city_input
    temp = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]
    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]
    condition = response["weather"][0]["description"].title()
    sunrise = datetime.fromtimestamp(response["sys"]["sunrise"]).strftime('%H:%M:%S')
    sunset = datetime.fromtimestamp(response["sys"]["sunset"]).strftime('%H:%M:%S')

    col1, col2 = st.columns([1.2, 1], gap="large")

    with col1:
        st.header(f"🌦️ Weather in {name}")
        st.metric("Temperature", f"{temp}°C", f"Feels like {feels_like}°C")
        st.metric("Humidity", f"{humidity}%")
        st.metric("Wind Speed", f"{wind_speed} m/s")
        st.write(f"Condition: {condition}")
        st.write(f"Sunrise: {sunrise} | Sunset: {sunset}")

        st.markdown("---")
        st.header("🤖 Health Precautions & Lifestyle Tips")
        st.markdown(f"""
        ### 🩺 Health Precautions
        - Current condition: {condition}. Avoid prolonged outdoor exposure if air quality is poor.
        - Temperature: {temp}°C (feels like {feels_like}°C) — stay hydrated.
        - Humidity: {humidity}% — drink enough water to prevent dehydration.
        
        ### 👕 Clothing Tips
        - Light, breathable fabrics (cotton, linen), light-colored clothing, sunglasses or hat.
        
        ### 🍴 Food & Hydration
        - Eat hydrating foods: watermelon, cucumber, oranges, leafy greens.
        - Avoid heavy, oily, or spicy foods.
        
        ### 🌈 Lifestyle & Activity
        - Exercise in early morning or evening.
        - Reduce outdoor exposure during extreme heat/cold or poor air quality.
        """)

    # --- Map Section using PyDeck (without Mapbox token) ---
    with col2:
        st.header("🗺️ Your Location on Map")
        df = pd.DataFrame({'lat': [lat], 'lon': [lon], 'label': [f"{name} 📍"]})
        view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=11, pitch=30)
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position=["lon", "lat"],
            get_color=[255, 0, 0, 200],
            get_radius=800,
            pickable=True
        )
        deck = pdk.Deck(
            map_style="light",  # Use built-in light style (no Mapbox token needed)
            initial_view_state=view_state,
            layers=[layer],
            tooltip={"text": "{label}"}
        )
        st.pydeck_chart(deck, use_container_width=True)

else:
    st.error(f"Error fetching weather: {response.get('message')}")



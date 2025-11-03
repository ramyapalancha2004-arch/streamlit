import streamlit as st
import requests
import pandas as pd
import pydeck as pdk
from datetime import datetime

st.set_page_config(page_title="🌤️ Smart Weather + Map Advisor", layout="wide")

st.title(" Smart Weather + Map Advisor")

st.subheader(" Location Detection")

try:
    location_data = requests.get("https://ipinfo.io/json", timeout=5).json()
    loc = location_data["loc"].split(",")
    lat, lon = float(loc[0]), float(loc[1])
    city = location_data.get("city", "Unknown")
    st.success(f" Location detected: {city} (Lat: {lat}, Lon: {lon})")
except Exception:
    st.error(" Couldn't detect automatically. Please enter manually:")
    lat = st.number_input("Latitude", value=17.385)
    lon = st.number_input("Longitude", value=78.486)
    city = "Manual Entry"


API_KEY = "98c4c53a9dbd06ec77bbc029cd164faa"  
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=10).json()
except requests.exceptions.RequestException:
    st.error(" Unable to connect to OpenWeather API. Please check your network.")
    st.stop()

if response.get("cod") == 200:
    
    name = response.get("name", city)
    temp = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]
    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]
    condition = response["weather"][0]["description"].title()
    sunrise = datetime.fromtimestamp(response["sys"]["sunrise"]).strftime('%H:%M:%S')
    sunset = datetime.fromtimestamp(response["sys"]["sunset"]).strftime('%H:%M:%S')

  
    col1, col2 = st.columns([1, 1], gap="large")

    
    with col1:
        st.markdown("###  Current Weather Details")
        st.metric(" Location", name)
        st.metric(" Temperature", f"{temp}°C", f"Feels like {feels_like}°C")
        st.metric(" Humidity", f"{humidity}%")
        st.metric(" Wind Speed", f"{wind_speed} m/s")
        st.write(f"**Condition:** {condition}")
        st.write(f" **Sunrise:** {sunrise}")
        st.write(f" **Sunset:** {sunset}")

        st.markdown("---")
        st.markdown("###  Smart AI Weather + Health Advice")

        
        st.markdown(f"""
        ####  Health Precautions
        - **Condition:** {condition}. If it's hazy or dusty, avoid prolonged outdoor exposure.  
        - **Temperature:** {temp}°C (feels like {feels_like}°C) — stay hydrated and rest in cool areas.  
        - **Humidity:** {humidity}% — drink enough water to prevent dehydration.  
        - Sensitive individuals (asthma/allergies) should wear a mask outdoors if air quality is low.  

        ####  Clothing Tips
        - Choose light, breathable fabrics (cotton, linen).  
        - Prefer light-colored clothes to reflect sunlight.  
        - Use sunglasses or a wide-brimmed hat if sunny.  

        ####  Food & Lifestyle Recommendations
        - Eat hydrating foods: **watermelon, cucumber, oranges, leafy greens**.  
        - Avoid oily and spicy foods in high humidity.  
        - Exercise early morning or evening when it’s cooler.  
        - Keep windows slightly open for ventilation if staying indoors.  
        """)

    
    with col2:
        st.markdown("###  Your Location on Map")

        df = pd.DataFrame({'lat': [lat], 'lon': [lon], 'label': [f"{name} 📍"]})

        view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=10, pitch=45)

        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position=["lon", "lat"],
            get_color=[255, 0, 0, 200],
            get_radius=800,
            pickable=True
        )

    
        deck = pdk.Deck(
            map_style=None,
            initial_view_state=view_state,
            layers=[layer],
            tooltip={"text": "{label}"}
        )

        st.pydeck_chart(deck, use_container_width=True)

else:
    st.error(" Unable to fetch weather data. Please check your API key or internet connection.")



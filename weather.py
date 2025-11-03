import streamlit as st
from streamlit_js_eval import get_geolocation
import requests

st.set_page_config(page_title=" WeatherSense", layout="wide")

WEATHER_API_KEY = "65b9ebfde30d0bbd0e38a973a638f850"

st.title(" WeatherSense — Real Feel Weather Assistant")
st.markdown("Get *real-time weather* and *natural comfort insights* ")
st.divider()

if "location_data" not in st.session_state:
    st.session_state.location_data = None

if st.session_state.location_data is None:
    with st.spinner(" Detecting your location... please allow browser permission"):
        loc = get_geolocation()
        if loc:
            st.session_state.location_data = loc
            st.rerun()
        else:
            st.stop()

loc = st.session_state.location_data
lat = loc.get("coords", {}).get("latitude")
lon = loc.get("coords", {}).get("longitude")

if not lat or not lon:
    st.stop()

st.success(f" Location detected — Latitude: {lat:.4f}, Longitude: {lon:.4f}")


weather_url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
)

try:
    res = requests.get(weather_url, timeout=10)
    res.raise_for_status()
    data_we = res.json()
except requests.exceptions.RequestException as e:
    st.error(f" Unable to fetch weather data: {e}")
    st.stop()


city = data_we.get("name", "Unknown Area")  
weather_info = data_we.get("weather", [{}])[0]
weather_desc = weather_info.get("description", "N/A").title()
icon = weather_info.get("icon", "01d")

main = data_we.get("main", {})
temp = main.get("temp", "N/A")
humidity = main.get("humidity", "N/A")
wind_speed = data_we.get("wind", {}).get("speed", 0)
icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"


col_map, col_weather = st.columns([1.2, 1.3])

with col_map:
    st.subheader(" Your Location")
    st.map([{"lat": lat, "lon": lon}])

with col_weather:
    st.subheader(f" Weather — {city}")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(icon_url, width=90)
    with c2:
        st.markdown(f" Condition: **{weather_desc}**")
        st.metric(" Temperature", f"{temp}°C")
        st.metric(" Humidity", f"{humidity}%")
        st.metric(" Wind Speed", f"{wind_speed} m/s")


st.divider()
st.subheader(" Natural Comfort Summary")

if isinstance(temp, (int, float)):
    summary = ""
    
    if temp < 0:
        summary = (
            " Extremely cold! Wear thermal layers, insulated jackets, gloves, and a hat. "
            "Stay indoors if possible; frostbite risk. Keep extremities covered."
        )
        st.info(summary)
    elif 0 <= temp < 10:
        summary = (
            " Very cold — dress warmly with a coat, scarf, and gloves. "
            "Limit prolonged outdoor exposure and keep moving to stay warm."
        )
        st.warning(summary)
    elif 10 <= temp < 18:
        summary = (
            " Cool and pleasant — a light jacket or sweater is recommended. "
            "Good for outdoor activities; carry an extra layer for evenings."
        )
        st.info(summary)
    elif 18 <= temp < 26:
        summary = (
            " Ideal weather — wear comfortable clothes like t-shirts and trousers. "
            "Perfect for outdoor exercise and work."
        )
        st.success(summary)
    elif 26 <= temp < 32:
        if humidity > 70:
            summary = (
                " Warm and humid — wear breathable cotton clothes. "
                "Stay hydrated and avoid strenuous outdoor activity during peak heat."
            )
            st.warning(summary)
        else:
            summary = (
                " Slightly warm — light, breathable clothing is recommended. "
                "Drink water regularly."
            )
            st.info(summary)
    elif 32 <= temp < 38:
        summary = (
            " Hot — wear loose, light clothing, a hat, and sunglasses. "
            "Drink plenty of water and avoid heavy outdoor work."
        )
        st.warning(summary)
    else:
        summary = (
            " Extreme heat! Minimal light clothing; stay in shaded or air-conditioned areas. "
            "Avoid direct sun exposure — risk of heatstroke."
        )
        st.error(summary)

    if "rain" in weather_desc.lower():
        st.info(" Carry an umbrella or raincoat. Stay dry to avoid colds.")
    if "snow" in weather_desc.lower():
        st.info(" Wear waterproof boots and warm clothing. Be careful on slippery surfaces.")
    if wind_speed > 10:
        st.info(" Strong winds — wear windproof jackets and secure loose items.")
else:
    st.warning(" Unable to determine temperature.")





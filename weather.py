import streamlit as st
import requests

st.set_page_config(page_title="Weather App 🌦️", page_icon="☁️", layout="centered")

st.title("🌦️ Weather Forecast Dashboard")
st.caption("Check live weather updates for any city!")

st.divider()


city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    if city:
        api_key = "023929d60b86c8b64be38dcef7fcd7d3"  # Replace with your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            res = requests.get(url)
            data = res.json()

            if res.status_code == 200:
                temp = data["main"]["temp"]
                weather = data["weather"][0]["main"]
                description = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]
                country = data["sys"]["country"]

                st.subheader(f" Location: {city.title()}, {country}")
                st.metric(label=" Temperature", value=f"{temp} °C")
                st.metric(label=" Humidity", value=f"{humidity} %")
                st.metric(label=" Wind Speed", value=f"{wind} m/s")
                st.write(f"**Weather:** {weather} — _{description}_")

                condition = description.lower()

                if "rain" in condition:
                    st.info(" **Suggested Plan:** Looks like rain today! Carry an umbrella and stay safe on wet roads.")
                    st.warning("🩺 **Doctor's Precautions:** Keep yourself dry and drink warm fluids.")

                elif "clear" in condition:
                    st.success(" **Suggested Plan:** Perfect day for outdoor activities or a walk!")
                    st.info("🩺 **Doctor's Precautions:** Use sunscreen and stay hydrated.")

                elif "cloud" in condition:
                    st.info(" **Suggested Plan:** It’s cloudy today — a relaxing indoor day!")
                    st.warning("🩺 **Doctor's Precautions:** Maintain good ventilation at home.")

                elif "mist" in condition or "fog" in condition:
                    st.warning(" **Suggested Plan:** Drive carefully — low visibility ahead.")
                    st.info("🩺 **Doctor's Precautions:** Use a mask outdoors and avoid long exposure.")

                else:
                    st.write(" **Suggested Plan:** Have a great day ahead! ")

            else:
                st.error(" City not found! Please check the spelling and try again.")

        except Exception as e:
            st.error(f" Error: {e}")

st.divider()


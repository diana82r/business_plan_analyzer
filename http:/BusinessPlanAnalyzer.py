import streamlit as st
import openai
import os

# گرفتن کلید API از فایل secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def analyze_idea(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # یا "gpt-4" اگه دسترسی داری
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای طرح‌های سرمایه‌گذاری هستید."},
            {"role": "user", "content": f"طرح سرمایه‌گذاری من اینه:\n{text}\nلطفاً یک تحلیل کامل انجام بده."}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

st.title("💼 تحلیل‌گر هوشمند طرح سرمایه‌گذاری")
user_input = st.text_area("✍️ خلاصه طرح سرمایه‌گذاری خود را وارد کنید:")

if st.button("🔍 تحلیل ایده"):
    if user_input.strip() == "":
        st.warning("لطفاً ابتدا خلاصه‌ای وارد کنید.")
    else:
        result = analyze_idea(user_input)
        st.markdown("### 🔍 تحلیل ایده")
        st.write(result)

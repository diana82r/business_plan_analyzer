import streamlit as st
import openai
import os

# تنظیم کلید API از محیط (از طریق Secrets در Streamlit Cloud)
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_idea(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # یا "gpt-4" اگه بهش دسترسی داری
        messages=[
            {"role": "system", "content": "تو یک تحلیل‌گر مالی حرفه‌ای هستی."},
            {"role": "user", "content": text}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

# رابط کاربری
st.title("💼 تحلیل‌گر هوشمند طرح سرمایه‌گذاری")
user_input = st.text_area("خلاصه طرح سرمایه‌گذاری خود را وارد کنید:")

if st.button("تحلیل ایده"):
    if user_input.strip():
        result = analyze_idea(user_input)
        st.success(result)
    else:
        st.warning("لطفاً یک متن وارد کنید.")

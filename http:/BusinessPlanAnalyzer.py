import streamlit as st
import openai
import os

# گرفتن API Key از Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_idea(text):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # یا "gpt-4" اگر دسترسی داری
        messages=[
            {"role": "system", "content": "تو یک تحلیل‌گر مالی با تجربه هستی. لطفاً طرح زیر را تحلیل کن:"},
            {"role": "user", "content": text}
        ],
   temperature=0.7
    )
    return response.choices[0].message.content

# رابط کاربری Streamlit
st.title("💼 تحلیل‌گر هوشمند طرح سرمایه‌گذاری")
user_input = st.text_area("✍️ خلاصه طرح سرمایه‌گذاری خود را وارد کنید:")

if st.button("🔍 تحلیل ایده"):
    if user_input.strip():
        result = analyze_idea(user_input)
        st.success(result)
    else:
        st.warning("لطفاً ابتدا یک طرح وارد کنید.") 

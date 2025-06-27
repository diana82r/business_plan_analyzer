import streamlit as st
import openai

st.title("تحلیل‌گر هوشمند طرح سرمایه‌گذاری")

openai.api_key = st.secrets["OPENAI_API_KEY"]

def analyze_idea(text):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
{"role": "system", "content": "تو یک مشاور مالی حرفه‌ای هستی. طرح‌های سرمایه‌گذاری را دقیق تحلیل کن."},
            {"role": "user", "content": f"این طرح را تحلیل کن:\n{text}"}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

user_input = st.text_area("خلاصه طرح سرمایه‌گذاری خود را وارد کنید")

if st.button("تحلیل ایده"):
    if not user_input.strip():
        st.warning("لطفاً خلاصه طرح را وارد کنید.")
else:
        with st.spinner("در حال تحلیل..."):
            result = analyze_idea(user_input)
            st.success("نتیجه تحلیل:")
            st.write(result)

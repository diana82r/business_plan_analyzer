import streamlit as st

st.title("تحلیل‌گر طرح سرمایه‌گذاری")

# بخش ورودی متن
user_input = st.text_area("خلاصه طرح سرمایه‌گذاری خود را اینجا وارد کنید")

# دکمه تحلیل
if st.button("تحلیل ایده"):
    if user_input.strip() == "":
        st.warning("لطفا خلاصه طرح خود را وارد کنید.")
    else:
        # اینجا صدا زدن تابع تحلیل و نمایش نتیجه
        result = analyze_idea(user_input)  # فرض می‌کنیم این تابع تحلیل داره
        st.write("نتایج تحلیل:")
        st.write(result)

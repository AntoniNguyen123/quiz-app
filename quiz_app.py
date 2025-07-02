#!/usr/bin/env python
# coding: utf-8

# In[6]:


#get_ipython().system(' pip install streamlit')


# In[3]:


import streamlit as st

questions = [
    {"question": "1. Thủ đô Việt Nam là gì?", "options": ["Hà Nội", "TP.HCM", "Huế"], "answer": "Hà Nội"},
    {"question": "2. Python là gì?", "options": ["Ngôn ngữ lập trình", "Trình duyệt", "Hệ điều hành"], "answer": "Ngôn ngữ lập trình"},
]

def run_quiz(questions):
    st.title("🧠 Trắc nghiệm Kiến thức")
    score = 0
    for i, q in enumerate(questions):
        st.subheader(q["question"])
        answer = st.radio("Chọn 1 đáp án:", q["options"], key=f"q{i}")
        if answer == q["answer"]:
            score += 1
        st.write("---")
    
    if st.button("✅ Nộp bài"):
        st.success(f"Bạn trả lời đúng {score}/{len(questions)} câu!")

if __name__ == "__main__":
    run_quiz(questions)


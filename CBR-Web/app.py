import streamlit as st
from data import load_case_database
from logic import find_similar_cases

st.set_page_config(page_title="CBR 案例推荐系统", layout="centered")

st.title("🚇 城市轨道灾害案例推荐系统")
st.markdown("请输入一个新案例的信息，我们将推荐相似案例及其应对措施。")

# 用户输入
cost = st.number_input("成本等级（Cost，整数1-6）", min_value=1.0, max_value=6.0, step=1.0)
duration = st.number_input("建设工期（Duration，单位月）", min_value=0.5, max_value=60.0, step=0.5)
year = st.number_input("项目年份（Year）", min_value=2000, max_value=2030, step=1)
stories = st.number_input("楼层数（Stories）", min_value=1, max_value=50, step=1)
type_choice = st.selectbox("项目类型（Type）", options=["New", "Refurb", "Extension"])

if st.button("🔍 开始比对"):
    query_case = {
        "Cost": cost,
        "Duration": duration,
        "Year": year,
        "Stories": stories,
        "Type": type_choice
    }

    cases = load_case_database()
    top_cases = find_similar_cases(cases, query_case)

    st.success("匹配完成，以下是最相似的 5 个案例：")
    st.table(top_cases[["ID", "Similarity", "Response"]].reset_index(drop=True))

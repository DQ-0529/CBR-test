import pandas as pd

def load_case_database():
    return pd.DataFrame([
        {"ID": "C1", "Cost": 3, "Duration": 2, "Year": 2021, "Stories": 3, "Type": "New", "Response": "安装自动喷水灭火系统"},
        {"ID": "C2", "Cost": 5, "Duration": 1.5, "Year": 2020, "Stories": 2, "Type": "Refurb", "Response": "加设钢结构支撑框架"},
        {"ID": "C3", "Cost": 4, "Duration": 3, "Year": 2019, "Stories": 5, "Type": "New", "Response": "优化疏散路线设计"},
        {"ID": "C4", "Cost": 2, "Duration": 2.5, "Year": 2022, "Stories": 1, "Type": "Extension", "Response": "增设监测传感器网络"},
        {"ID": "C5", "Cost": 3, "Duration": 2, "Year": 2020, "Stories": 2, "Type": "New", "Response": "配置应急供电系统"},
        {"ID": "C6", "Cost": 6, "Duration": 1, "Year": 2023, "Stories": 4, "Type": "Refurb", "Response": "更新通风与排烟系统"},
        {"ID": "C7", "Cost": 2, "Duration": 2, "Year": 2021, "Stories": 2, "Type": "Extension", "Response": "建立灾后重建计划"},
        {"ID": "C8", "Cost": 4, "Duration": 3, "Year": 2022, "Stories": 3, "Type": "New", "Response": "提升地震防护能力"},
        {"ID": "C9", "Cost": 5, "Duration": 1.5, "Year": 2023, "Stories": 4, "Type": "Refurb", "Response": "优化结构冗余设计"},
        {"ID": "C10", "Cost": 2, "Duration": 2, "Year": 2018, "Stories": 1, "Type": "Extension", "Response": "布设火灾应急广播系统"},
    ])

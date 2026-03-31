import streamlit as st
from backend.weather_advisor import get_hko_weather
from backend.remove_bg import process_clothing_image
from PIL import Image
import os

# 設定網頁標題
st.set_page_config(page_title="StyleLoop HK - AI 造型師", page_icon="👗")

st.title("👗 StyleLoop HK")
st.subheader("你的智能衣櫥管理助手")

# --- 第一部分：天氣穿搭建議 ---
st.write("---")
st.header("🌦️ 今日穿搭建議")
if st.button("獲取天文台即時建議"):
    advice = get_hko_weather()
    st.info(advice)

# --- 第二部分：AI 一鍵去背 ---
st.write("---")
st.header("📸 數位化你的衣物")
st.write("上傳衣服照片，AI 將自動為你移除背景並存入虛擬衣櫥。")

uploaded_file = st.file_uploader("選擇一張衣服照片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 顯示原圖
    image = Image.open(uploaded_file)
    st.image(image, caption='原始照片', use_container_width=True)
    
    if st.button("開始 AI 去背"):
        # 暫存檔案並處理
        with open("temp_input.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        with st.spinner('AI 正在努力工作中...'):
            process_clothing_image("temp_input.png")
            
        # 顯示結果
        if os.path.exists("temp_input_no_bg.png"):
            result_img = Image.open("temp_input_no_bg.png")
            st.image(result_img, caption='去背完成！已加入數位衣櫥', use_container_width=True)
            st.success("處理成功！這件衣服已準備好進行虛擬配搭。")
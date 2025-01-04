import streamlit as st
import pandas as pd
import os
import openai

# API 키 불러오기
openai_api_key = st.secrets["api_keys"]["openai_api_key"]

# OpenAI API 키 설정
# openai.api_key = openai_api_key

# st.write("API Key is securely loaded.")
os.environ["OPENAI_API_KEY"] = openai_api_key

from gpt_structure import dd_generate_gpt4_basic
from knowledge_structure import *

st.set_page_config(
    page_title="SNU 3년후 나에게 편지쓰기 - 편지 & Knowledge Generation",
    page_icon="📩",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items= {
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': 'SNU 3년 후 나에게 편지쓰기 실험용 플랫폼',
    }
)

# @st.cache_data(ttl=30)
# def load_data(file_name):
#   df = pd.read_csv(file_name)
#   return df

maindf = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSeQnWRH6pThLkTrMYyOVL561Q-LAnJR_OxUEQE5gocZz3X2gFJw5aVcdvAHTr_HhUY8CtzgPabndyM/pub?gid=394540533&single=true&output=csv")
predf = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSYnWYG2W6fNP06ZktMZW_bjn2fqnn19qX_prnaMlUUGDTuKsEk5Vy6EygTxNRRfy2VFfcWdyv3r479/pub?gid=1670265382&single=true&output=csv")

predf.dropna(inplace=True)

streamlit_style = """
			<style>
			@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

			html, body, [class*="css"],g {
			  font-family: Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
      }
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

st.title('SNU 3년 후 나에게서의 편지 Generation Test')
st.markdown('---')

system_lib_file = './data/prompt_template/sys_template.txt'
f = open(system_lib_file, "r")
sys_prompt = f.read()
f.close()

with st.form('prompt_selector'):
  user_name = st.radio(
            "Select User Name 👉",
            key="user_name",
            options = maindf['참여자 코드를 입력해 주세요.'].unique()
  )


  submit = st.form_submit_button('Submit')

if submit:
  pre_test = predf[predf['참여자 코드를 입력해 주세요.'] == user_name]
  main_test = maindf[maindf['참여자 코드를 입력해 주세요.'] == user_name]
  
  letter_to_gpt = "[A letter to my future self three years from now]" + "\n" + main_test.iloc[0,86]
  st.write(letter_to_gpt)

  with st.spinner('Wait for it...'):
    future_profile = future_profile_generate(main_test)
    demo = demo_generate(main_test)
    bfi = bfi_generate(main_test)
    pvq = pvq_generate(main_test)
    love_hate = love_hate_generate(main_test)
    career_status = career_status_generate(pre_test)
    career_insight = career_insight_generate(pre_test)

    knowledge = future_profile
    knowledge += "\n"
    knowledge += demo
    knowledge += "\n"
    knowledge += bfi
    knowledge += "\n"
    knowledge += pvq
    knowledge += "\n"
    knowledge += love_hate
    knowledge += "\n"
    knowledge += "\n"
    knowledge += career_status
    knowledge += "\n"
    knowledge += "\n"
    knowledge += career_insight
    knowledge += "\n"

    st.subheader("Knowledge")
    st.write(knowledge)
    st.write('---------------------------------')
    reply1 = dd_generate_gpt4_basic(sys_prompt,knowledge,letter_to_gpt)
    st.subheader("3년 후 나의 답장 1")
    st.write(reply1)
    st.write('---------------------------------')
    reply2 = dd_generate_gpt4_basic(sys_prompt,knowledge,letter_to_gpt)
    st.subheader("3년 후 나의 답장 2")
    st.write(reply2)
    st.write('---------------------------------')
    reply3 = dd_generate_gpt4_basic(sys_prompt,knowledge,letter_to_gpt)
    st.subheader("3년 후 나의 답장 3")
    st.write(reply3)
    st.write('---------------------------------')

import streamlit as st
import random
st.set_page_config(page_title="FINDFOOD", page_icon="🍣")
st.title('姐姐吃什么呀？🥰')
# 初始化一个食物列表，如果session_state里没有的话
if 'food_list' not in st.session_state:
    st.session_state.food_list = ['潮汕牛肉汤粉', '烧烤', '麦当劳', '塔斯汀', '炒粉', '酱香饼', '甘草水果']
# 允许用户自定义列表
with st.expander("FOOD LIST"):
    new_food = st.text_input('是谁发现好吃的啦：')
    if st.button('ADD FOOD'):
        if new_food and new_food not in st.session_state.food_list:
            st.session_state.food_list.append(new_food)
        if st.button('清空LIST'):
            st.session_state.food_list = []
        st.write('当前LIST:', st.session_state.food_list)
# 选择按钮
if st.button('🫵就决定是你啦！'):
    if st.session_state.food_list:
        chosen_food = random.choice(st.session_state.food_list)
        st.success(f'## 今天要被欧尼吃掉的是： {chosen_food} ！')
    else:
        st.error('肚子空空，请姐姐多多探索好吃爱吃的吧！')

import streamlit as st
from dogpredict import app as dog_app
from dog_explain import app as dog_explain_app
from plantpredict import app as plant_app
from plantexplain import app as plant_explain_app

st.set_page_config(page_title='AI Web App', page_icon='🤖', layout='wide')

if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def set_page(page_name):
    st.session_state.page = page_name

if st.session_state.page == 'Home':
    st.title('🏠 Welcome to My AI Plant and Dog Prediction Project')
    st.write('''
    เลือกหน้าด้วยปุ่มด้านล่าง
    ''')

    col2, col3 = st.columns(2)
    with col2:
        st.button('📘 ไปแนวทางพัฒนาโมเดลPlant Predictor', on_click=set_page, args=('Plant Explain',))
    with col3:
        st.button('📘 ไปแนวทางพัฒนาโมเดลDog Predictor', on_click=set_page, args=('Dog Explain',))

    st.divider()
    st.markdown('### รายชื่อสมาชิก')
    st.write('Sec 5')
    st.write('นาย พนมกร หยกสิทธิชัยกุล(Panomkorn yoksittichaikul) 6704062662241 CSB ')
    st.write('นาย ธนภัทร มณีเรือง(Tanaphat Maneeraung) 6704062662267 CSB')

elif st.session_state.page == 'Dog Explain':
    if st.button('🔙 กลับ Home', on_click=set_page, args=('Home',)):
        pass
    dog_explain_app()

elif st.session_state.page == 'Plant Explain':
    if st.button('🔙 กลับ Home', on_click=set_page, args=('Home',)):
        pass
    plant_explain_app()

elif st.session_state.page == 'Dog Predictor':
    if st.button('🔙 กลับ Home', on_click=set_page, args=('Home',)):
        pass
    dog_app()

elif st.session_state.page == 'Plant Predictor':
    if st.button('🔙 กลับ Home', on_click=set_page, args=('Home',)):
        pass
    plant_app()

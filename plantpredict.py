import streamlit as st
import joblib
from pathlib import Path

@st.cache_data
def load_crop_model():
    model_path = Path(__file__).parent / 'crop_model.pkl'
    if not model_path.exists():
        raise FileNotFoundError('crop_model.pkl not found in app directory')
    return joblib.load(model_path)


def app():
    st.title('🌿 Plant Predictor')
    st.write('หน้านี้ใช้งานโมเดล `crop_model.pkl` เพื่อทำนายพืชที่เหมาะสมตามค่าดิน/สภาพอากาศ')

    st.markdown('### 1) กรอกค่าปัจจัยส่งเข้าโมเดล')
    col1, col2, col3 = st.columns(3)
    with col1:
        n = st.slider('N (ไนโตรเจน)', 0, 140, 90)
        p = st.slider('P (ฟอสฟอรัส)', 0, 140, 40)
        k = st.slider('K (โพแทสเซียม)', 0, 140, 40)
    with col2:
        temperature = st.slider('อุณหภูมิ (°C)', 0.0, 45.0, 20.0)
        humidity = st.slider('ความชื้น (%)', 10.0, 100.0, 80.0)
        ph = st.slider('ค่า pH ของดิน', 3.0, 9.0, 6.5)
    with col3:
        rainfall = st.slider('ปริมาณฝน (มม.)', 0.0, 300.0, 200.0)

    if st.button('🔍 ทำนายพืชจากโมเดล'):
        try:
            model = load_crop_model()
            features = [[n, p, k, temperature, humidity, ph, rainfall]]
            prediction = model.predict(features)[0]
            st.success(f'✅ โมเดลทำนายว่าเหมาะกับพืช: **{prediction}**')
            st.info('โมเดลเป็น VotingClassifier ที่ใช้ SVC + KNN + DecisionTree')
        except Exception as e:
            st.error(f'เกิดข้อผิดพลาดขณะโหลดโมเดล: {e}')

    st.divider()
    st.write('เคล็ดลับ: ใช้ค่าปุ๋ย (N, P, K) และสภาพอากาศใกล้เคียงจริง เพื่อได้คำทำนายที่แม่นยำ')

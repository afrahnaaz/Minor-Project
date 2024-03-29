import streamlit as st
st.set_page_config(page_title="Software Developer Salary Prediction", page_icon="📉", layout="wide", initial_sidebar_state="expanded", menu_items=None)

# st.set_page_config(page_title='Machine Learning Model Trainer', page_icon=None, )


from PIL import Image
from predict import show_predict_page
from explore_page import show_explore_page

col1, col2, col3 = st.columns([3, 6, 1])
with col1:
    sru_logo = st.image(Image.open('sr-university-logo.png'), use_column_width='auto', output_format='png')

with col2:
    pass

with col3:
    ai_logo = st.image(Image.open('SRU_AI_LOGO_digital_art_x4_colored_toned.jpg'), width=80, output_format='png')



image = Image.open('icon.png')
img = st.sidebar.image(image, width=80, use_column_width=80)
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

about  = st.sidebar.markdown('''
## ABOUT
This is Machine Learning Web Application that helps in Predicting the Salary of a Software Developer based on their Experience, Location, Education Level, Languages known etc,\n

Code: [source](https://github.com/AmoghvarshRaju/software-salary-prediction)\n

Web Application made with [Streamlit](https://streamlit.io/)  
Team:
- [A.Amogh Varsh Raju](https://www.linkedin.com/in/amogh-varsh-raju-ambati-408475199)
- [T.Kavya Sree](https://www.linkedin.com/in/kavya-takkarsu-869a17190)
- [Afra Naaz](https://www.linkedin.com/in/afrah-naaz-324434231)
- [I.Sai dev](https://instagram.com/b_a_bb_l_u?igshid=YmMyMTA2M2Y=)
''')

sru_logo = st.sidebar.image(Image.open('sr-university-logo.png'), use_column_width='auto', output_format='png')
if page == "Predict":
    show_predict_page()

else:
    show_explore_page()
    
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

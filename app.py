import streamlit as st
import base64
import random
import time
from modelClasses import emotionRecogniationSystem, musicRecommendationSystem

st.markdown("## 🎵 MoodTune", text_alignment='center')
st.markdown("### Music that matches your mood", text_alignment='center')

if 'status' not in st.session_state:
    st.session_state.status = 0

if 'res_emotion' not in st.session_state:
    st.session_state.res_emotion = 'N/A'

if 'action_btn1' not in st.session_state:
    st.session_state.action_btn1 = False

if 'action_btn2' not in st.session_state:
    st.session_state.action_btn2 = False

if 'action_btn3' not in st.session_state:
    st.session_state.action_btn3 = False

if 'musicSystem' not in st.session_state:
    st.session_state['musicSystem'] = musicRecommendationSystem('9cc6000b894141e0a25ca44d7648762c', '9beb79b537b243fbba425420f556df25', 'http://127.0.0.1:9090/callback')

if 'songs' not in st.session_state:
    st.session_state.songs = None


def getBase64Image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def buttonClick(active: str):
    if active == 'action_btn1':
        emotionRecogniationSystem().run()
    st.session_state[active] = True
    if st.session_state['status'] >= 66:
        st.session_state['status'] = 100
        return
    st.session_state['status'] += 33

def analyzeEmotion():
    ans = random.choice(['HAPPY', 'NEUTRAL'])
    st.session_state['res_emotion'] = ans
    buttonClick(active = 'action_btn2')

def recommendeSong():
    buttonClick(active = 'action_btn3')
    st.session_state['songs'] = st.session_state['musicSystem'].recommendeSong('Lover Song', n = 3)
    time.sleep(0.7)

    
bar = st.progress(st.session_state['status'])

with st.columns(1, border = True,)[0]:
    
    st.space(10)
    
    st.html(
        f'''
            <div style="display: flex; justify-content: center;">
                <img style = "width: 50px" src="data:image/png;base64,{getBase64Image("camera.png")}">
            </div>
        '''
    )

    st.space(5)

    if not st.session_state['action_btn1']:
        with st.container(horizontal = True, horizontal_alignment ='center'):
            st.button(f'TURN ON', on_click = buttonClick, args = ('action_btn1',), icon = 'spinner')
    else:
        st.markdown('#### EMOTION IS CAPTURED', text_alignment='center')

    st.space(10)

emotion = {
    'HAPPY': '😊',
    'NEUTRAL': '😐',
}

with st.columns(1, border = True)[0]:

    st.space(5)
    
    with st.container(horizontal = True,horizontal_alignment='distribute'):

        if st.session_state['res_emotion'] == 'N/A':
            st.markdown(f"#### N/A")
        else:
            st.markdown(f"### { emotion[st.session_state['res_emotion']] }")
            with st.columns(1)[0]:
                st.html(
                    f'<p style = "font-size: 15px; margin-bottom: -20px; color: grey; font-weight: bold;">MOOD</p>'
                )
                st.markdown(f"##### {st.session_state['res_emotion']}")

            st.space(3)


        if st.session_state['action_btn1'] and not(st.session_state['action_btn2']):
            st.button('ANALYZE EMOTION', on_click = analyzeEmotion, icon = 'spinner')
            
        if st.session_state['action_btn2']: 
            st.button('RECOMMENDE', icon = 'spinner', on_click=recommendeSong)
    
    st.space(5)

st.space(3)

if st.session_state['action_btn3']:
    st.markdown('#### RECOMMENDED SONGS')

    for i, song in enumerate(st.session_state['songs']):
        with st.container(horizontal = True, border = True, horizontal_alignment = 'distribute', vertical_alignment = 'center'):
            st.image(song['albumUrl'], width = 70)

            with st.container(vertical_alignment = 'center', gap = 'xxsmall'):
                st.markdown(f"{song['name']}")
                st.markdown(f"{song['artistName']}")

            st.button(
                "PLAY",key=f"playBtn{i + 1}",icon=":material/play_arrow:", on_click = st.session_state['musicSystem'].playSong,
                args=(song["uri"],), width=150
            )
        
    if st.session_state['playBtn1']:
        print(f"First Song Played")

    if st.session_state['playBtn2']:
        print(f"Secound Song Played")

    if st.session_state['playBtn3']:
        print(f"Third Song Played")
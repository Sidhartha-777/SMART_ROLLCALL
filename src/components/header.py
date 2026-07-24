import streamlit as st

def header_home():
    logo_url="https://img.icons8.com/ios-filled/512/ffffff/face-id.png"
    st.markdown(f"""
                    <div style='display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px'>
                        <img src='{logo_url}' style='height:100px;' />
                        <h1 style='text-align:center; color:#E0E3FF'>SMART<br/>ROLLCALL</h1>
                    </div>
                """,unsafe_allow_html=True)
    
def header_dashboard():
    st.markdown(f"""
                    <div style='display:flex; align-items:center; justify-content:center; gap:10px;'>
                        <h2 style='text-align:left; color:#5865F2'>SMART<br/>ROLLCALL</h2>
                    </div>
                """,unsafe_allow_html=True)
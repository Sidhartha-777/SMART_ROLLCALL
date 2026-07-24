import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of the subject")
    sub_id=st.text_input("Enter Subject Code",placeholder="E.g. CS2002")
    sub_name=st.text_input("Enter Subject Name",placeholder="E.g. Operating Systems")
    sub_section=st.text_input("Enter Subject Section",placeholder="E.g. S1")

    if st.button("Create Subject Now",type='primary',width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject Created Successfully!!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please Fill All The Details")
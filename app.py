# Local Multimodal AI Chat - Multimodal chat application with local models
# Copyright (C) 2024 Leon Sander
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import streamlit as st
import sqlite3
import sys
from database_operations import init_db

from llm_chains import load_normal_chain, load_pdf_chat_chain
from streamlit_mic_recorder import mic_recorder
from utils import get_timestamp, load_config, get_avatar
from image_handler import handle_image
from audio_handler import transcribe_audio
from pdf_handler import add_documents_to_db
from html_templates import css
from database_operations import load_last_k_text_messages, save_text_message, save_image_message, save_audio_message, load_messages, get_all_chat_history_ids, delete_chat_history
config = load_config()


@st.cache_resource
def load_chain():
    if st.session_state.get('pdf_chat', False):
        print("loading pdf chat chain")
        return load_pdf_chat_chain()
    return load_normal_chain()

def toggle_pdf_chat():
    st.session_state['pdf_chat'] = True
    clear_cache()

def get_session_key():
    session_key = st.session_state.get('session_key', 'new_session')
    if session_key == "new_session":
        st.session_state['new_session_key'] = get_timestamp()
        return st.session_state['new_session_key']
    return session_key

def delete_chat_session_history():
    delete_chat_history(get_session_key())
    st.session_state['session_index_tracker'] = "new_session"

def clear_cache():
    st.cache_resource.clear()

def log_debug_message(message):
    print(message, file=sys.stderr)

def main():
    init_db()
    if 'db_conn' not in st.session_state:
        st.session_state['db_conn'] = sqlite3.connect(config["chat_sessions_database_path"], check_same_thread=False)
    

    st.title("Efor Multimodal Local Chat App")
    st.write(css, unsafe_allow_html=True)
    
    # nitialize all session state variables 
    st.session_state.setdefault('session_key', 'new_session')
    st.session_state.setdefault('new_session_key', None)
    st.session_state.setdefault('session_index_tracker', 'new_session')
    st.session_state.setdefault('pdf_chat', False)
    st.session_state.setdefault('audio_uploader_key', 0)
    st.session_state.setdefault('pdf_uploader_key', 1)

    # Sidebar logic
    st.sidebar.title("Chat Sessions")
    chat_sessions = ["new_session"] + get_all_chat_history_ids()
    index = chat_sessions.index(st.session_state.get('session_index_tracker', 'new_session'))
    st.sidebar.selectbox("Select a chat session", chat_sessions, key="session_key1", index=index)  # Unique key argument

   #the next toggcode le is just for another form of button
    #pdf_toggle_col, voice_rec_col = st.sidebar.columns(2) 
    #pdf_toggle_col.button("Enable PDF Chat", on_click=toggle_pdf_chat, key="pdf_button")  # Unique key argument

    #with voice_rec_col: 
        #voice_recording = mic_recorder(start_prompt="Record Audio", stop_prompt="Stop recording", just_once=True, key="voice_recorder")

    #delete_chat_col, clear_cache_col = st.sidebar.columns(2) 
    #delete_chat_col.button("Delete Chat Session", on_click=delete_chat_session_history, key="delete_button")  # Unique key argument
    #clear_cache_col.button("Clear Cache", on_click=clear_cache, key="clear_cache_button")  # Unique key argument

    #index = chat_sessions.index(st.session_state.session_index_tracker)
    # st.sidebar.selectbox("Select a chat session", chat_sessions, key="session_key2", index=index)  # Unique key argument
    pdf_toggle_col, voice_rec_col = st.sidebar.columns(2)
    pdf_toggle_col.toggle("PDF Chat", key="pdf_chat", value=False)
    with voice_rec_col:
        voice_recording=mic_recorder(start_prompt="Record Audio",stop_prompt="Stop recording", just_once=True)
    delete_chat_col, clear_cache_col = st.sidebar.columns(2)

    delete_chat_col.button("Delete Chat Session", on_click=delete_chat_session_history, key="delete_button_2")  # Unique key argument
    clear_cache_col.button("Clear Cache", on_click=clear_cache, key="clear_cache_button_2")  # Unique key argument

    chat_container = st.container()
    user_input = st.chat_input("Type your message here", key="user_input")
    
    
    uploaded_audio = st.sidebar.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"],
key=st.session_state.audio_uploader_key)
    uploaded_image = st.sidebar.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])
    uploaded_pdf = st.sidebar.file_uploader("Upload a pdf file", accept_multiple_files=True, 
                                            key=st.session_state.pdf_uploader_key, type=["pdf"], on_change=toggle_pdf_chat)

    if uploaded_pdf:
        with st.spinner("Processing pdf..."):
            add_documents_to_db(uploaded_pdf)
            st.session_state.pdf_uploader_key += 2

    if uploaded_audio:
        transcribed_audio = transcribe_audio(uploaded_audio.getvalue())
        print(transcribed_audio)
        llm_chain = load_chain()
        llm_answer = llm_chain.run(user_input = "Summarize this text: " + transcribed_audio, chat_history=[])
        save_audio_message(get_session_key(), "human", uploaded_audio.getvalue())
        save_text_message(get_session_key(), "ai", llm_answer)
        st.session_state.audio_uploader_key += 2

    if voice_recording:
        transcribed_audio = transcribe_audio(voice_recording["bytes"])
        print(transcribed_audio)
        llm_chain = load_chain()
        llm_answer = llm_chain.run(user_input = transcribed_audio, 
                                   chat_history=load_last_k_text_messages(get_session_key(), config["chat_config"]["chat_memory_length"]))
        save_audio_message(get_session_key(), "human", voice_recording["bytes"])
        save_text_message(get_session_key(), "ai", llm_answer)

    
    if user_input:
        if uploaded_image:
            with st.spinner("Processing image..."):
                llm_answer = handle_image(uploaded_image.getvalue(), user_input)
                save_text_message(get_session_key(), "human", user_input)
                save_image_message(get_session_key(), "human", uploaded_image.getvalue())
                save_text_message(get_session_key(), "ai", llm_answer)
                user_input = None


        if user_input:
            llm_chain = load_chain()
            llm_answer = llm_chain.run(user_input = user_input, 
                                       chat_history=load_last_k_text_messages(get_session_key(), config["chat_config"]["chat_memory_length"]))
            save_text_message(get_session_key(), "human", user_input)
            save_text_message(get_session_key(), "ai", llm_answer)
            user_input = None


    if (st.session_state.session_key != "new_session") != (st.session_state.new_session_key != None):
        with chat_container:
            chat_history_messages = load_messages(get_session_key())

            for message in chat_history_messages:
                with st.chat_message(name=message["sender_type"], avatar=get_avatar(message["sender_type"])):
                    if message["message_type"] == "text":
                        st.write(message["content"])
                    if message["message_type"] == "image":
                        st.image(message["content"])
                    if message["message_type"] == "audio":
                        st.audio(message["content"], format="audio/wav")

        if (st.session_state.session_key == "new_session") and (st.session_state.new_session_key != None):
            st.rerun()

if __name__ == "__main__":
    main()

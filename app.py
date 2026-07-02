import streamlit as st
import time
from speech import transcribe_audio
from utils import save_uploaded_file, save_transcript


# as st is using sortcut name 

st.title("speech recognition")
st.write("upload an audio file to convert to text file using whisper openAI:")
#file upload button creat code
# down code is using for creat button and message for user view 
audio_file = st.file_uploader("choose an audio file to upload",
type=["mp3", "wav", "m4a"])


if audio_file:
    st.success("file uploaded successfully")
    file_path = save_uploaded_file(audio_file)
        
    if st.button("convert to text"):
      try:
            with st.spinner("converting audio.."):
               start_time = time.time()
               
               text = transcribe_audio(file_path)
               end_time = time.time()
               processing_time = end_time - start_time
               st.info(f"processing_time: {processing_time:.1f} seconds") 
            
            st.success("transcription completed")
            
            st.subheader("transcription")
            
            st.text_area(

                    label="result",
                    value=text,
                    height=250,
            )
            st.download_button(
                label="download text",
                data=text,
                file_name="transcription.txt",
                mime="text/plain"
            )
            
      except Exception as e:
          st.error(f"error: {e}")   
          
          text= transcribe_audio(file_path)
          transcript_path = save_transcript(text)
          st.success(f"transcript saved successfully")
          st.write(f"saved file: {transcript_path}")
           
           
           
           
            # save the uploaded file to a temporary location






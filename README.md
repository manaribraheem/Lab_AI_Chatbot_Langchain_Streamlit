 ## Steps to Set Up Multimodal AI Chat 

1. **PC Setup**:
   - Download Visual C++ Build tools from this [link](https://stackoverflow.com/questions/40504552/how-to-install-visual-c-build-tools).
   - Create a parent folder named Lab_AI.
   - Navigate to the Lab_AI folder in the command prompt.
   - Create a virtual environment named chat_venv.

2. **Clone Repository**:
   - Clone the repository from [here](https://github.com/manaribraheem/Lab_AI_Chatbot_Langchain_Streamlit).
   - After cloning, you will have the Lab_AI_Chatbot_Langchain_Streamlit folder and the chat_venv inside the Lab_AI folder.

3. **Download LLM (Language Model)**:
   - Download the Mistral LLM inside the models folder in Lab_AI_Chatbot_Langchain_Streamlit.
   - Choose between the large model from [TheBloke](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf) or the medium model.
   - Modify the config.yaml accordingly by commenting out the model you didn't choose.

4. **Image Embedding Models**:
   - Download the image embedding model mmproj-model-f16.gguf from [here](https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main) inside the llava folder.
   - Additionally, download the ggml-model-q5_k.gguf from [here](https://huggingface.co/mys/ggml_llava-v1.5-13b/blob/main/ggml-model-q5_k.gguf) to handle image embedding.

5. **Adjust Model Paths**:
   - Update the paths for the downloaded models in the config.yaml file under the llava_model section.
   - Set llava_model_path to "./models/llava/llava_ggml-model-q5_k.gguf".
   - Set clip_model_path to "./models/llava/mmproj-model-f16.gguf".

6. **Image and Question Chat Enhancement**:
   - This setup enables image dragging and asking questions. Future improvements can include integrating image display in the frontend.

7. **PDF Handling**:
   - For handling PDFs in English, use BAAI/bge-large-en-v1.5. Adjust code implementation if using "Cohere/Cohere-embed-multilingual-v3.0".

8. **Audio Transcription**:
   - Use Whisper from Hugging Face for audio transcription without manual downloading.
   - Update the transcription function to summarize using models like Bart or T5 and adjust the audio handler function accordingly.
   - Set the device (CPU or GPU) as per requirements.

9. **Additional Requirement**:
   - Install the sentence-transformers version 2.2.2.

**Have fun exploring the Multimodal AI Chat capabilities!**  

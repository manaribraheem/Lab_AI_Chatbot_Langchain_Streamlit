## Multimodal AI Chat Setup Guide

### 1. PC Setup
- **Visual C++ Build Tools**: Download and install the **Visual C++ Build Tools** from the provided link. These tools are essential for building C++ code on Windows.
- **Parent Folder Creation**: Create a parent folder named **Lab_AI** (or any other name you prefer) to organize your project files.
- **Command Prompt Navigation**: Open a command prompt or terminal and navigate to the **Lab_AI** folder using the `cd` command.

### 2. Virtual Environment Setup
- Create a virtual environment named **chat_venv** using your preferred Python environment manager (e.g., `venv`, `conda`, or `pipenv`). Activate the virtual environment.

### 3. Repository Cloning
- Clone the repository from the provided link. After cloning, your directory structure should look like this:
    ```
    Lab_AI/
    ├── Lab_AI_Chatbot_Langchain_Streamlit/
    ├── chat_venv/
    ```

### 4. Download the LLM (Language Model)
- Inside the **Lab_AI_Chatbot_Langchain_Streamlit/models** folder, download the **Mistral LLM**. Choose between the large model from **TheBloke** or the medium model.
- Modify the **config.yaml** file accordingly by commenting out the model you didn't choose.

### 5. Image Embedding Models
- Download the image embedding model **mmproj-model-f16.gguf** from the provided link and place it inside the **llava** folder.
- Additionally, download the **ggml-model-q5_k.gguf** from the provided link to handle image embedding.

### 6. Update Model Paths
- Open the **config.yaml** file and update the paths for the downloaded models under the **llava_model** section:
    - Set `llava_model_path` to `"./models/llava/llava_ggml-model-q5_k.gguf"`.
    - Set `clip_model_path` to `"./models/llava/mmproj-model-f16.gguf"`.

### 7. Image and Question Chat Enhancement
- The setup enables image dragging and asking questions. Consider future improvements, such as integrating image display in the frontend for a more interactive experience.

### 8. PDF Handling
- For handling PDFs in English, use the model **BAAI/bge-large-en-v1.5**. Adjust your code implementation accordingly.
- If you prefer a multilingual approach, consider using **Cohere/Cohere-embed-multilingual-v3.0**.

### 9. Audio Transcription
- Utilize the **Whisper** model from Hugging Face for audio transcription without manual downloading.
- Update the transcription function to summarize using models like **Bart** or **T5**. Adjust the audio handler function accordingly.
- Set the device (CPU or GPU) based on your requirements.

### 10. Additional Requirement
- Install **sentence-transformers** version 2.2.2 using `pip install sentence-transformers`.

### 11. Explore and Have Fun!
- With this setup, you're ready to explore the exciting capabilities of the **Multimodal AI Chat**. Feel free to experiment and enjoy!

Remember to adapt these instructions to your specific environment and preferences. Happy coding! 🚀🤖

---

Feel free to reach out if you have any further questions or need assistance! 😊

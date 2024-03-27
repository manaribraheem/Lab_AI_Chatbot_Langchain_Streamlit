# Efor Multimodal AI Chat

## Steps
1. In this work, we use chroma data base
- In your Pc  create a Parent folder Lab_AI
- in cmd , navigate to this folder Lab_AI
- create a virtual environement chat_venv  
2.  Clone the repo https://github.com/manaribraheem/Lab_AI_Chatbot_Langchain_Streamlit--> (you will have Lab_AI_Chatbot_Langchain_Streamlit and chat_venv inside Lab_AI)
3.Download the LLM : mistral inside the folder models inside Lab_AI_Chatbot_Langchain_Streamlit
  the large one
 [TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf))
the medium one 
[Mistral-7B-Instruct-v0.1-GGUF from TheBloke](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf))
Modefiy  the config.yaml accordingly : comment what you didn't take
example
ctransformers:
  model_path:
    small: "./models/mistral-7b-instruct-v0.1.Q2_K.gguf"
    #larg : "./models/mistral-7b-instruct-v0.1.Q5_K_S.gguf"
Also  change in  llm_chains.py  the variable small to what you didn't comment in config file
def create_llm(model_path = config["ctransformers"]["model_path"]["small"], model_type = config["ctransformers"]["model_type"], model_config = config["ctransformers"]["model_config"]):
    llm = CTransformers(model=model_path, model_type=model_type, config=model_config)
    return llm
  
4. inside Lab_AI_Chatbot_Langchain_Streamlit/models/llava donwload image embedding model mmproj-model-f16.gguf from here 
 https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main

(go to files and versions in llava-v1.5-7b ) and  download also another llama model to handel image embedding ggml-model-q5_k.gguf in the llava folder  from https://huggingface.co/mys/ggml_llava-v1.5-13b/blob/main/ggml-model-q5_k.gguf

5. Adjust in  config.yaml  the path for these 2 models according to what you downloaded
llava_model:
  llava_model_path: "./models/llava/llava_ggml-model-q5_k.gguf"
  clip_model_path: "./models/llava/mmproj-model-f16.gguf"
This  part  enable you to  drag an  image and ask question..  we can improve  the code to chat with the image and to display the image in the frontend later
6. Pdf handling : I'm using BAAI/bge-large-en-v1.5 for english only .  if we take the other one "Cohere/Cohere-embed-multilingual-v3.0" we should  change the implementing code , you need to do nothing here
7. for audio: you need to  do nothing : Whisper for audio would be used from huggingface without manuel donwloading .   This model with the function would transcribe the speach . If we want to summerize, we should use another model as bart or T5  and  change the funtion in audio handler.
Don't forget to set the device accordingly


def transcribe_audio(audio_bytes):

    #device = "cuda:0" if torch.cuda.is_available() else "cpu"
                                                    
    device = "cpu"
   
    pipe = pipeline(
   
        task="automatic-speech-recognition",
   
        model=config["whisper_model"],
   
        chunk_length_s=30,
   
        device=device,
    )
   
n requirements

sentence-transformers==2.2.2


  

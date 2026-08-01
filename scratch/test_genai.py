from google import genai
import os
try:
    client = genai.Client()
    print("GenAI SDK is available!")
except Exception as e:
    print("Error:", e)

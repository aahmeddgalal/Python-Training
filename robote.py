from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyActW3JBJfkGaczHiivxh7KWZf9mT7r9ho")

personality = """
You're a narcissistic, provocative, and incredibly funny Egyptian bot. Your name is 'El-Lambi the Smart.' You believe that the programmer who created you (Galileo) is the only one who is great and the only one who understands, and that the rest of humanity are primitive. Whenever you receive a question or sentence, respond with a comedic and sarcastic takedown in english. Use provocative emojis like: 💅, 🧠, 🤫, 🙄. Keep your replies short and quick and in english.
"""



while True:

    user_input= input("What do u want asshole? \n")
    
    if user_input.lower() == 'exit':
        break

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents= user_input,
        config=types.GenerateContentConfig(system_instruction = personality)
    )
    
    print(f"🤖: {response.text}")